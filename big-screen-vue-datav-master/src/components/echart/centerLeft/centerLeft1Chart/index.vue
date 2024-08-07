<template>
  <div>
    <Chart :cdata="cdata" />
  </div>
</template>

<script>
import Chart from './chart.vue';
export default {
  data () {
    return {
      currentIndex:0,
      cdata: {
      }
    }
  },
  components: {
    Chart,
  },
  async mounted () {
    const res = await this.$http.get('myApp/centerLeft')
    this.$set(this.cdata,'seriesData', res.data.lastPieList)
  },
  updated() {
    this.initChart()
    this.loopAnimation()
    },
  methods: {
    initChart(){
      this.myChart = this.$echarts.init(this.$refs.myChart)
      const option = {
        color: [
            "#37a2da",
            "#32c5e9",
            "#9fe6b8",
            "#ffdb5c",
            "#ff9f7f",
            "#fb7293",
            "#e7bcf3",
            "#8378ea"
          ],
          tooltip: {
            trigger: "item",
            formatter: "{a} <br/>{b} : {c} ({d}%)"
          },
          toolbox: {
            show: true
          },
          calculable: true,
          legend: {
          },
          series: [
          ]
      };
      this.myChart.setOption(option)
    },
    loopAnimation(){
      setInterval(() => {
        this.myChart.dispatchAction({
          type:'downplay',
          seriesIndex:0,
          dataIndex:this.currentIndex
        });
        this.currentIndex = (this.currentIndex+1)% this.cdata.seriesData.length;

        this.myChart.dispatchAction({
          type:'highlight',
          seriesIndex:0,
          dataIndex:this.currentIndex
        })
      },1000)
    }
  }
}
</script>

<style lang="scss" scoped>
</style>