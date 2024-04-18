const express = require("express");
const cors = require("cors");
const {get_commodity_data} = require('./express_service/getPrice')
const {get_cn_futures} = require('./express_service/get_cn_symbols')
const {get_display_data} = require("./express_service/get_display_data")
const {data_update} = require("./express_service/daily_update")
const {get_econ_indicators} = require("./express_service/get_econ_indicators")
const {get_forex} = require("./express_service/get_forex")
const axios = require("axios");
const app = express();
const moment = require('moment');

app.use(express.json()); // for parsing JSON data in request bodies
app.use(cors()); // enable CORS for all routes

const server = require("http").createServer(app)

// 格式化数据为对象数组
function formatData(data, start) {
    const startDate = moment(start);
    const formattedData = [];

    for (let i = 0; i < data.length; i++) {
        const currentDate = startDate.clone().add(i, 'months').format('YYYY-MM-DD');
        formattedData.push({ date: currentDate, value: data[i] });
    }

    return formattedData;
}


app.get('/cn_futures', (req, res) => {
  const symbol = req.query.name;

  get_commodity_data(symbol, (data) => {
    if (data.length > 0) {
      res.json(data)
    } else {
      res.status(404).json({error: 'commodity data is empty'})
    }
  })
})

app.get('/all_cn_futures', (req, res) => {
  const symbol = req.query.name;

  get_cn_futures(symbol, (data) => {
    if (data.length > 0) {
      res.json(data)
    } else {
      res.status(404).json({error: 'all futures data not fount'})
    }
  })
})

app.get('/display', (req, res) => {
  const symbol = req.query.name

  get_display_data(symbol, (data) => {
    if (data.length > 0) {
      res.json(data)
    } else {
      res.status(404).json({error: 'display data not found'})
    }
  })
})

app.get('/data_update', (req, res) => {
  const symbol = req.query.name

  data_update(symbol, (data) => {
    res.json({})
  })
})

app.get('/econ_indicators', (req, res) => {

  get_econ_indicators((data) => {
    res.json(data)
  })
})

app.get('/forex', (req, res) => {

  get_forex((data) => {
    res.json(data)
  })
})

app.get('/cnbs', async (req, res) => {
  // 中国宏观杠杆率

  const response = await axios.get(`http://127.0.0.1:8080/api/public/macro_cnbs`)
  const modifiedResponse = response.data.map(item => {
    const modifiedItem = { 时间: item['年份'] }; // 添加"时间"键值对，并复制"年份"值
    delete item['年份']; // 删除"年份"键

    // 进行其他键名的替换
    modifiedItem['居民部门'] = item['居民部门'];
    modifiedItem['非金融企业'] = item['非金融企业部门'];
    modifiedItem['实体经济'] = item['实体经济部门'];
    modifiedItem['政府部门'] = item['政府部门'];
    modifiedItem['中央政府'] = item['中央政府'];
    modifiedItem['地方政府'] = item['地方政府'];
    modifiedItem['金融资产方'] = item['金融部门资产方'];
    modifiedItem['金融负债方'] = item['金融部门负债方'];

    return { ...modifiedItem };
  });
  res.json(modifiedResponse)
})

app.get('/commodity_price', async (req, res) => {
  const response = await axios.get(`http://127.0.0.1:8080/api/public/macro_china_qyspjg`)
  res.json(response.data)
})

app.get('/social_rz', async (req, res) => {
  const response = await axios.get(`http://127.0.0.1:8080/api/public/macro_china_shrzgm`)
  res.json(response.data)
})

app.get('/CPI_monthly', async (req, res) => {
  const response = await axios.get(`http://127.0.0.1:8080/api/public/macro_china_cpi_monthly`)
  res.json(response.data)
})

app.get('/money_supply', async (req, res) => {
  const response = await axios.get(`http://127.0.0.1:8080/api/public/macro_china_money_supply`)
  let result = response.data
  result.reverse()
  result = formatData(result, '2008-01-01')
  res.json(result)
})

app.get('/PMI', async (req, res) => {
  const response = await axios.get(`http://127.0.0.1:8080/api/public/macro_china_pmi_yearly`)
  const result = formatData(response.data, '2005-02-01')
  res.json(result)
})

const PORT = 3628
server.listen(PORT, () => {
  console.log(`Server listening on PORT ${PORT}`)
})