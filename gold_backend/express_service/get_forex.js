const sqlite3 = require('sqlite3').verbose();
const fs = require('fs');
const exec = require('child_process').exec;

const db = new sqlite3.Database('gold_backend/slingshot_api/api/tv/cn_fx_live.db', (err) => {
  // console.log(fs.existsSync('../database/all_cn_futures.db'))
  if (err) {
    console.error('Error opening database:', err.message);
  } else {
    console.log('Connected to the SQLite database.');
  }
});

function get_forex(callback) {
  const db_loc = __dirname.toString().replace('\\express_service', '\\slingshot_api\\api\\tv')
  exec('python forex.py', {cwd: db_loc}, (error, stdout, stderr) => {
    if (error) {
        console.error(`exec error: ${error}`);
        return;
    }
    console.log(`stdout: ${stdout}`);
    console.error(`stderr: ${stderr}`);
    const sql = "SELECT * FROM live";
    db.all(sql, (err, rows) => {
      if (err) {
        callback([]);
      } else {
        const data = rows.map((row) => ({
            Symbol: row.pair,
            Price: row.price,
            PercentChange: row.pct_change,
            Change: row.change,
            Bid: row.bid,
            Ask: row.ask,
            High: row.high,
            Low: row.low,
            TechRating: row.rating
        }));
        callback(data)
      }
    })
  })
}

module.exports = {get_forex};