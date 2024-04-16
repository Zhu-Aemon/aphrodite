const express = require("express");
const cors = require("cors");
const {get_commodity_data} = require('./express_service/getPrice')
const {get_cn_futures} = require('./express_service/get_cn_symbols')
const {get_display_data} = require("./express_service/get_display_data")
const {data_update} = require("./express_service/daily_update")
const {get_econ_indicators} = require("./express_service/get_econ_indicators")
const {get_forex} = require("./express_service/get_forex")
const app = express();
app.use(express.json()); // for parsing JSON data in request bodies
app.use(cors()); // enable CORS for all routes

const server = require("http").createServer(app)

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

const PORT = 3628
server.listen(PORT, () => {
  console.log(`Server listening on PORT ${PORT}`)
})