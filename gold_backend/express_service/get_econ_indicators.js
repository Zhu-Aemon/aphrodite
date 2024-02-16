const sqlite3 = require('sqlite3').verbose();
const fs = require('fs');

const db = new sqlite3.Database('gold_backend/database/econ_indicators.db', (err) => {
  // console.log(fs.existsSync('../database/all_cn_futures.db'))
  if (err) {
    console.error('Error opening database:', err.message);
  } else {
    console.log('Connected to the SQLite database.');
  }
});

function get_econ_indicators(symbol, callback) {
  const sql = "SELECT * FROM T" + symbol;
  db.all(sql, (err, rows) => {
    if (err) {
      callback([]);
    } else {
      const data = rows.map((row) => ({
          US: row.US,
          CN: row.CN,
          EU: row.EU,
          JP: row.JP,
          DE: row.DE,
          GB: row.GB,
          FR: row.FR,
          RU: row.RU,
          CA: row.CA,
          IT: row.IT,
          AU: row.AU
      }));
      callback(data)
    }
  })
}

module.exports = {get_econ_indicators};