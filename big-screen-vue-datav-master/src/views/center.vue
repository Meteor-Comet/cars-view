<template>
  <div id="center">
    <div class="up">
      <div
          class="bg-color-black item"
      >
        <p class="ml-3 colorBlue fw-b fs-xl" style="font-size: 15px">车辆总数据</p>
        <div style="text-align: center;line-height: 2;">
          {{this.result.sumCar}}
        </div>
      </div>
      <div
        class="bg-color-black item"
      >
        <p class="ml-3 colorBlue fw-b fs-xl" style="font-size: 15px">车辆最高销售额</p>
        <div style="text-align: center;line-height: 2;">
          {{this.result.highVolume}}
        </div>
      </div>
      <div
        class="bg-color-black item"
      >
        <p class="ml-3 colorBlue fw-b fs-xl" style="font-size: 15px">销售最多车型</p>
        <div style="text-align: center;line-height: 2;">
          {{this.result.topCar}}
        </div>
      </div>
      <div
        class="bg-color-black item"
      >
        <p class="ml-3 colorBlue fw-b fs-xl" style="font-size: 15px">销售最多车型</p>
        <div style="text-align: center;line-height: 2;">
          {{this.result.mostModel}}
        </div>
      </div>
      <div
        class="bg-color-black item"
      >
        <p class="ml-3 colorBlue fw-b fs-xl" style="font-size: 15px">车型最多品牌</p>
        <div style="text-align: center;line-height: 2;">
          {{this.result.mostBrand}}
        </div>
      </div>
      <div
        class="bg-color-black item"
      >
        <p class="ml-3 colorBlue fw-b fs-xl" style="font-size: 15px">车辆平均价格</p>
        <div style="text-align: center;line-height: 2;">
          {{this.result.averagePrice}}万
        </div>
      </div>
    </div>
    <div class="down">
      <div class="ranking bg-color-black">
        <span>
          <icon name="chart-pie" class="text-icon"></icon>
        </span>
        <span class="fs-xl text mx-2 mb-1 pl-3" style="font-size: 18px;font-weight: bold">汽车品牌榜-品牌在售车型数</span>
        <dv-scroll-ranking-board class="dv-scr-rank-board mt-1" :config="ranking" v-bind:key="ranking.data[0].value" />
      </div>
      <div class="percent">
        <div class="item bg-color-black">
          <span style="font-size: 15px">油车占有率</span>
          <CenterChart
            :id="rate[0].id"
            :tips="rate[0].tips"
            :colorObj="rate[0].colorData"
          />
        </div>
        <div class="item bg-color-black">
          <span style="font-size: 15px">电车占有率</span>
          <CenterChart
            :id="rate[1].id"
            :tips="rate[1].tips"
            :colorObj="rate[1].colorData"
          />
        </div>
        <div class="water" style="text-align: center">
          <span class="fs-xl text mx-2 mb-1 pl-3" style="font-size: 15px">混合车型占有率</span>
          <dv-water-level-pond class="dv-wa-le-po" :config="water" v-bind:key="water.data[0]"/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import CenterChart from '@/components/echart/center/centerChartRate'

export default {
  data() {
    return {
      result: '',
      ranking: {
        data: [
          {
            name:'默认',
            value: 1
          }
        ],
        carousel: 'single',
        unit: '种'
      },
      water: {
        data: [24, 45],
        shape: 'round',
        formatter: '{value}%',
        waveNum: 3
      },
      // 通过率和达标率的组件复用数据
      rate: [
        {
          id: 'centerRate1',
          tips: 60,
          colorData: {
            textStyle: '#3fc0fb',
            series: {
              color: ['#00bcd44a', 'transparent'],
              dataColor: {
                normal: '#03a9f4',
                shadowColor: '#97e2f5'
              }
            }
          }
        },
        {
          id: 'centerRate2',
          tips: 40,
          colorData: {
            textStyle: '#67e0e3',
            series: {
              color: ['#faf3a378', 'transparent'],
              dataColor: {
                normal: '#ff9800',
                shadowColor: '#fcebad'
              }
            }
          }
        }
      ]
    }
  },
  components: {
    CenterChart
  },
  async mounted(){
    const res = await this.$http.get('myApp/center')
    this.result = res.data
    this.$set(this.ranking,'data',res.data.lastSortList)
    this.$set(this.rate[0],'tips',res.data.oilRate)
    this.$set(this.rate[1],'tips',res.data.electricRate)
    this.$set(this.water,'data',[res.data.mixRate,res.data.mixRate])
  }
}
</script>

<style lang="scss" scoped>
#center {
  display: flex;
  flex-direction: column;
  .up {
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    .item {
      border-radius: 6px;
      padding-top: 8px;
      margin-top: 8px;
      width: 32%;
      height: 70px;
      .dv-dig-flop {
        width: 150px;
        height: 30px;
      }
    }
  }
  .down {
    padding: 6px 4px;
    padding-bottom: 0;
    width: 100%;
    display: flex;
    height: 255px;
    justify-content: space-between;
    .bg-color-black {
      border-radius: 5px;
    }
    .ranking {
      padding: 10px;
      width: 59%;
      .dv-scr-rank-board {
        height: 225px;
      }
    }
    .percent {
      width: 40%;
      display: flex;
      flex-wrap: wrap;
      .item {
        width: 50%;
        height: 120px;
        span {
          margin-top: 8px;
          font-size: 14px;
          display: flex;
          justify-content: center;
        }
      }
      .water {
        width: 100%;
        .dv-wa-le-po {
          height: 120px;
        }
      }
    }
  }
}
</style>
