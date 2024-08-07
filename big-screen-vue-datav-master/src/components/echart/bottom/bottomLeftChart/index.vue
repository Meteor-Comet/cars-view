<template>
  <div>
    <div ref="chart" style="width: 100%; height: 450px;" v-bind:key="cdata.lineData[0]"></div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      cdata: {
        category: [],
        lineData: [],
        barData: [],
        rateData: []
      },
      myChart: null,
      intervalId: null,
      visibleColumns: 8, // 显示的列数
      currentIndex: 0, // 当前显示数据的起始索引
      barMin: null, // 左侧坐标轴最小值
      barMax: null, // 左侧坐标轴最大值
      lineMin: null, // 右侧坐标轴最小值
      lineMax: null // 右侧坐标轴最大值
    };
  },
  components: {
    // ...
  },
  async mounted () {
    const res = await this.$http.get('myApp/bottomLeft')
    this.$set(this.cdata,'category',res.data.brandList)
    this.$set(this.cdata,'lineData',res.data.priceList)
    this.$set(this.cdata,'barData',res.data.volumeList)

    this.calculateMinMax(); // 计算坐标轴的最小值和最大值
    this.initChart();
    this.startDataUpdateInterval();
  },
  updated() {
    this.initChart();
  },
  beforeDestroy() {
    clearInterval(this.intervalId);
  },
  methods: {
    calculateMinMax() {
      this.barMin = Math.min(...this.cdata.barData);
      this.barMax = Math.max(...this.cdata.barData);
      this.lineMin = Math.min(...this.cdata.lineData);
      this.lineMax = Math.max(...this.cdata.lineData);
    },
    initChart(){
      this.myChart = this.$echarts.init(this.$refs.chart);

      const option = {
          tooltip: {
            trigger: "axis",
            backgroundColor: "rgba(255,255,255,0.1)",
            axisPointer: {
              type: "shadow",
              label: {
                show: true,
                backgroundColor: "#7B7DDC"
              }
            }
          },
          legend: {
            data: ["销售数量", "NaN", "车辆价格"],
            textStyle: {
              color: "#B4B4B4",
              fontSize: 18
            },
            top: "0%"
          },
          grid: {
            x: "8%",
            width: "88%",
            y: "4%"
          },
          xAxis: {
            data: this.cdata.category.slice(this.currentIndex, this.currentIndex + this.visibleColumns),
            axisLine: {
              lineStyle: {
                color: "#B4B4B4",
              }
            },
            axisTick: {
              show: false
            },
            axisLabel: {
              show: true,
              interval: 0,
              fontSize: 16
            }
          },
          yAxis: [
            {
              type: 'value',
              // min: this.barMin, // 固定最小值
              max: 50000, // 固定最大值
              splitLine: { show: false },
              axisLine: {
                lineStyle: {
                  color: "#B4B4B4",
                }
              },
              axisLabel: {
                formatter: "{value}辆",
                fontSize: 15
              }
            },
            {
              type: 'value',
              // min: this.lineMin, // 固定最小值
              max: 40, // 固定最大值
              splitLine: { show: false },
              axisLine: {
                lineStyle: {
                  color: "#B4B4B4"
                }
              },
              axisLabel: {
                formatter: "{value}万元",
                fontSize: 15
              }
            }
          ],
          series: [
            {
              name: "车辆价格",
              type: "line",
              smooth: true,
              showAllSymbol: true,
              symbol: "emptyCircle",
              symbolSize: 12,
              yAxisIndex: 1,
              itemStyle: {
                normal: {
                  color: "#ee56ff"
                }
              },
              animationDuration: 2000, // 增加动画时长
              animationEasing: 'cubicOut', // 使用缓动函数
              data: this.cdata.lineData.slice(this.currentIndex, this.currentIndex + this.visibleColumns)
            },
            {
              name: "销售数量",
              type: "bar",
              barWidth: 30,
              itemStyle: {
                normal: {
                  barBorderRadius: 5,
                  color: new this.$echarts.graphic.LinearGradient(0, 0, 0, 1, [
                    { offset: 0, color: "#45f2ff" },
                    { offset: 1, color: "#26078f" }
                  ])
                }
              },
              data: this.cdata.barData.slice(this.currentIndex, this.currentIndex + this.visibleColumns)
            },

          ]
      };
      this.myChart.setOption(option);
    },
    startDataUpdateInterval() {
      const interval = 3000; // 轮播间隔时间，单位毫秒
      clearInterval(this.intervalId); // 清除之前的定时器
      this.intervalId = setInterval(() => {
        this.updateBarChartData();
      }, interval);
    },
    updateBarChartData() {
      // 平滑轮播
      const shiftAmount = 1; // 每次移动一个元素
      this.currentIndex = (this.currentIndex + shiftAmount) % (this.cdata.category.length - this.visibleColumns + 1);

      this.myChart.setOption({
        xAxis: {
          data: this.cdata.category.slice(this.currentIndex, this.currentIndex + this.visibleColumns)
        },
        series: [
          {
            data: this.cdata.lineData.slice(this.currentIndex, this.currentIndex + this.visibleColumns)
          },
          {
            data: this.cdata.barData.slice(this.currentIndex, this.currentIndex + this.visibleColumns)
          }
        ]
      });
    }
  }
};
</script>

<style lang="scss" scoped>
</style>
