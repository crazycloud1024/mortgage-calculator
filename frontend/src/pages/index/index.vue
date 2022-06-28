<template>
  <nut-form>
    <nut-form-item label="贷款总额(万)">
      <input class="nut-input-text" placeholder="100" type="text" />
    </nut-form-item>
    <nut-cell title="还款方式">
      <template v-slot:link>
        <nut-button size="small" type="info" style="margin-right: 10px" @click="
          () => {
            pay_type = true;
          }
        ">选择
        </nut-button>
        <nut-picker v-model:visible="pay_type" :columns="pay_types" title="还款方式" @change="change" @confirm="confirm">
        </nut-picker>
      </template>
    </nut-cell>
    <nut-cell title="还款年数">
      <template v-slot:link>
        <nut-button size="small" type="info" style="margin-right: 10px" @click="
          () => {
            show = true;
          }
        ">选择
        </nut-button>
        <nut-picker v-model:visible="show" :columns="columns" title="还款年数" @change="change" @confirm="confirm">
        </nut-picker>
      </template>
    </nut-cell>
    <nut-cell title="首次还款日期" :showIcon="true" :desc="date ? `${date}` : '请选择'" @click="openSwitch('isVisible')">
      <template v-slot:link>
        <nut-button size="small" type="info" style="margin-right: 10px" @click="
          () => {
            isVisible = true;
          }
        ">选择
        </nut-button>
      </template>
    </nut-cell>
    <nut-calendar v-model:visible="isVisible" :default-value="date" @close="closeSwitch('isVisible')"
      @choose="setChooseValue">
    </nut-calendar>
    <nut-form-item label="LPR(贷款市场报价利率)" >
      <input class="nut-input-text" placeholder="请输入利率" type="integer" v-model="state.lpr_value1" />
    </nut-form-item>
    <nut-form-item label="基点" >
      <input class="nut-input-text" placeholder="请输入基点" type="integer" v-model="state.lpr_value2" />
    </nut-form-item>
    <nut-form-item label="贷款利率">
      <input class="nut-input-text" placeholder="利率" v-model="state.lpr_value" type="integer" />
    </nut-form-item>
  </nut-form>

  <nut-button block type="info" @click="handleTap()">开始计算</nut-button>
</template>

<script lang="ts">
import { reactive, toRefs, ref } from "vue";
import Taro from "@tarojs/taro";
export default {
  name: "Index",
  components: {},
  setup() {
    const show = ref(false);
    const pay_type = ref(false);
    const desc = ref("");

    const pay_types = ref([
      { text: "等额本息（每月等额还款）", value: "pay_type1" },
      { text: "等额本金（每月递减还款）", value: "pay_type2" },
    ]);
    const columns = ref([
      { text: "1年", value: "1" },
      { text: "2年", value: "2" },
      { text: "3年", value: "3" },
      { text: "4年", value: "4" },
      { text: "5年", value: "5" },
      { text: "6年", value: "6" },
      { text: "7年", value: "7" },
      { text: "8年", value: "8" },
      { text: "9年", value: "9" },
      { text: "10年", value: "10" },
      { text: "11年", value: "11" },
      { text: "12年", value: "12" },
      { text: "13年", value: "13" },
      { text: "14年", value: "14" },
      { text: "15年", value: "15" },
      { text: "16年", value: "16" },
      { text: "17年", value: "17" },
      { text: "18年", value: "18" },
      { text: "19年", value: "19" },
      { text: "20年", value: "20" },
      { text: "21年", value: "21" },
      { text: "22年", value: "22" },
      { text: "23年", value: "23" },
      { text: "24年", value: "24" },
      { text: "25年", value: "25" },
      { text: "26年", value: "26" },
      { text: "27年", value: "27" },
      { text: "28年", value: "28" },
      { text: "29年", value: "29" },
      { text: "30年", value: "30" },
    ]);
    const confirm = ({ selectedValue, selectedOptions }) => {
      desc.value = selectedValue.join(",");
    };
    const change = ({ selectedValue, selectedOptions }) => {
      console.log(selectedValue);
    };

    const state = reactive({
      isVisible: false,
      date: "",
      text: "",
      pay_info: 0,
      lpr_value1: 0,
      lpr_value2: 0,
      lpr_value: 0,
    });
        const formData  = reactive({
      isVisible: false,
      date: "",
      text: "",
      pay_info: 0,
      lpr_value1: 0,
      lpr_value2: 0,
      lpr_value: 0,
    });
    const openSwitch = (param) => {
      state[`${param}`] = true;
    };
    const closeSwitch = (param) => {
      state[`${param}`] = false;
    };
    const setChooseValue = (param) => {
      state.date = param[3];
    };
    const select = (param: string) => {
      console.log(param);
    };

    const handleTap = () => {
      state.lpr_value = Number(state.lpr_value1) - Number(state.lpr_value2) / 100
      
      console.log(state.lpr_value, state.lpr_value1, state.lpr_value2)
      Taro.request({
        url: "http://127.0.0.1:8000/api/v1/lrp/equal_principal_interest",
        method: "POST",
        data: { "lpr_year_value": state.lpr_value },
      }).then(function (response) {
        state.pay_info = response.data;
        for (let obj in state.pay_info) {
          console.log((state.pay_info[obj][0]))
        }
      });
    };

    return {
      columns,
      show,
      desc,
      change,
      confirm,
      pay_type,
      pay_types,
      ...toRefs(state),
      openSwitch,
      closeSwitch,
      setChooseValue,
      select,
      handleTap,
      state,
    };
  },
};
</script>

<style lang="scss">
.index {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
</style>
