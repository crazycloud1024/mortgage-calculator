import { createApp } from 'vue'
import { Button, Toast } from '@nutui/nutui-taro';
import { Picker, Popup, OverLay } from '@nutui/nutui-taro';
import { Form,FormItem,Cell,CellGroup,Icon } from '@nutui/nutui-taro';
import { Calendar } from '@nutui/nutui-taro';

import './app.scss'

const app = createApp({
  onShow (options) {},
  // 入口组件不需要实现 render 方法，即使实现了也会被 taro 所覆盖
})

app.use(Button).use(Toast)
app.use(Picker);
app.use(Popup);
app.use(OverLay);
app.use(Form);
app.use(FormItem);
app.use(Cell);
app.use(CellGroup);
app.use(Icon);
app.use(Calendar);

export default app
