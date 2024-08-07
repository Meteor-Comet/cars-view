<template>
  <div>
    <Echart
      :options="options"
      id="centreLeft1Chart"
      ref="centreLeft1ChartRef"
      height="320px"
      width="260px"
    ></Echart>
  </div>
</template>

<script>
import Echart from '@/common/echart';

export default {
  data() {
    return {
      options: {},
      intervalId: null,
      currentIndex: 0,
    };
  },
  components: {
    Echart,
  },
  props: {
    cdata: {
      type: Object,
      default: () => ({}),
    },
  },
  watch: {
    cdata: {
      handler(newData) {
        this.options = {
          color: [
            "#37a2da",
            "#32c5e9",
            "#9fe6b8",
            "#ffdb5c",
            "#ff9f7f",
            "#fb7293",
            "#e7bcf3",
            "#8378ea",
          ],
          tooltip: {
            trigger: "item",
            formatter: "{a} <br/>{b} : {c}辆 ({d}%)",
          },
          toolbox: {
            show: false,
          },
          calculable: true,
          legend: {
            orient: "horizontal",
            icon: "circle",
            bottom: 0,
            x: "center",
            data: newData.xData,
            textStyle: {
              color: "#fffffe",
            },
          },
          series: [
            {
              name: "销售量占比统计",
              type: "pie",
              radius: [25, 80],
              roseType: "area",
              center: ["50%", "40%"],
              data: newData.seriesData,
              label: {
                normal: {
                  formatter: "{b}",
                  textStyle: {
                    fontSize: 15,
                    color: "#f6f5f5",
                  },
                },
              },
              labelLine: {
                normal: {
                  show: true, // 如果需要隐藏引导线，可以设置为 false
                  length: 5, // 缩短引导线的长度
                  length2: 10, // 调整引导线超出标签部分的长度
                },
              },
              emphasis: {
                itemStyle: {
                  shadowBlur: 10,
                  shadowOffsetX: 0,
                  label: {
                    show: true,
                  },
                },
              },
            },
          ],
        };

        // 初始化时选中第一个数据项
        this.handlePieSequentialSelect();
      },
      immediate: true,
      deep: true,
    },
  },
  methods: {
    startInterval() {
      const _self = this;
      // 应通过接口获取配置时间，暂时写死5s
      const time = 2000;
      if (this.intervalId !== null) {
        clearInterval(this.intervalId);
      }
      this.intervalId = setInterval(() => {
        _self.selectNextPieArea();
      }, time);
    },
    selectNextPieArea() {
      const length = this.cdata.seriesData.length;
      this.$nextTick(() => {
        try {
          const chart = this.$refs.centreLeft1ChartRef.chart;
          let nextIndex = (this.currentIndex + 1) % length;
          chart.dispatchAction({
            type: 'downplay',
            seriesIndex: 0,
            dataIndex: this.currentIndex,
          });
          chart.dispatchAction({
            type: 'highlight',
            seriesIndex: 0,
            dataIndex: nextIndex,
          });
          this.currentIndex = nextIndex;
        } catch (error) {
          console.log(error);
        }
      });
    },
    handlePieSequentialSelect() {
      this.$nextTick(() => {
        try {
          const chart = this.$refs.centreLeft1ChartRef.chart;
          const _self = this;
          setTimeout(() => {
            _self.selectNextPieArea();
          }, 0);
          // 移入区域，清除定时器、取消之前选中并选中当前
          chart.on('mouseover', function (params) {
            clearInterval(_self.intervalId);
            chart.dispatchAction({
              type: 'downplay',
              seriesIndex: 0,
              dataIndex: _self.currentIndex,
            });
            chart.dispatchAction({
              type: 'highlight',
              seriesIndex: 0,
              dataIndex: params.dataIndex,
            });
            _self.currentIndex = params.dataIndex;
          });
          // 移出区域重新按顺序选中数据项，并开启定时器
          chart.on('globalout', function () {
            _self.selectNextPieArea();
            _self.startInterval();
          });
          this.startInterval();
        } catch (error) {
          console.log(error);
        }
      });
    },
  },
};
</script>

<style lang="scss" scoped>
</style>
