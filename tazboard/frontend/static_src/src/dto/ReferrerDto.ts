import { ChartData } from 'chart.js'

export class ReferrerData {
  referrer!: string
  hits!: number
}

export class ReferrerDto {
  total!: number
  data!: Array<ReferrerData>

  static toChartdata (graph: ReferrerDto): ChartData {
    return {
      labels: graph.data.map((item) => item.referrer),
      datasets: [{
        label: 'Referrers',
        data: graph.data.map((item) => item.hits)
      }]
    }
  }
}
