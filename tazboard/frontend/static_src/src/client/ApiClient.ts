import { HistogramDto } from '@/dto/HistogramDto'
import { QueryParams, queryString } from '@/utils/urls'
import { ReferrerDto } from '@/dto/ReferrerDto'
import { ToplistDto } from '@/dto/ToplistDto'

export class HttpError extends Error {
  constructor (public response: Response) {
    super()
  }
}

export class BadRequest extends HttpError {
}

export class NotFound extends HttpError {
}

export class InternalServerError extends HttpError {
}

export class ApiClient {
  baseURL = '/api/v1/'

  async histogram (minDate: string, maxDate: string, msgId: number | null = null): Promise<HistogramDto> {
    return await this.request<HistogramDto>('histogram', 'GET', {
      msgId,
      min: minDate,
      max: maxDate
    })
  }

  async referrer (minDate: string, maxDate: string, msgId: number | null = null): Promise<ReferrerDto> {
    return await this.request<ReferrerDto>('referrer', 'GET', {
      msgId,
      min: minDate,
      max: maxDate
    })
  }

  async toplist (minDate: string, maxDate: string, limit = 10): Promise<ToplistDto> {
    return await this.request<ToplistDto>('toplist', 'GET', {
      min: minDate,
      max: maxDate,
      limit: limit
    })
  }

  async request<T> (path: string, method: string, queryParams: QueryParams = {}): Promise<T> {
    const response = await this.requestRaw(path, method, queryParams)

    if (!response.ok) {
      switch (response.status) {
        case 400:
          throw new BadRequest(response)
        case 404:
          throw new NotFound(response)
        case 500:
          throw new InternalServerError(response)
        default:
          throw new HttpError(response)
      }
    }

    return (await response.json()) as T
  }

  async requestRaw (path: string, method: string, queryParams: QueryParams = {}): Promise<Response> {
    return fetch(this.baseURL + path + queryString(queryParams), {
      method
    })
  }
}
