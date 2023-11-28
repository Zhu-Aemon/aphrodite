const sqlite3 = require('sqlite3').verbose();
const fs = require('fs');

const db = new sqlite3.Database('gold_backend/database/all_cn_futures.db', (err) => {
  // console.log(fs.existsSync('../database/all_cn_futures.db'))
  if (err) {
    console.error('Error opening database:', err.message);
  } else {
    console.log('Connected to the SQLite database.');
  }
});

function get_cn_futures(symbol, callback) {
  const sql = "SELECT * FROM " + symbol;
  db.all(sql, (err, rows) => {
    if (err) {
      callback([]);
    } else {
      const data = rows.map((row) => ({
          symbol: row.symbol,
          exchange: row.exchange,
          name: row.name
      }));
      callback(data)
    }
  })
}

module.exports = {get_cn_futures};