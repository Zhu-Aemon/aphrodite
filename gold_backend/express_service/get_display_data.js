const sqlite3 = require('sqlite3').verbose();

const db = new sqlite3.Database('gold_backend/database/cn_commodity.db', (err) => {
  if (err) {
    console.error('Error opening database:', err.message);
  } else {
    console.log('Connected to the SQLite database.');
  }
});

function get_display_data(symbol, callback) {
  const sql = "SELECT * FROM " + symbol;
  db.all(sql, (err, rows) => {
    if (err) {
      callback([]);
    } else {
      const data = rows.map((row) => ({
        time: row.date.slice(0, 10),
        open: row.open,
        high: row.high,
        low: row.low,
        close: row.close,
      }));
      callback(data)
    }
  })
}

module.exports = {get_display_data};