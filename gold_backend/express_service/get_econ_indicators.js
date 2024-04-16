const sqlite3 = require('sqlite3').verbose();
const fs = require('fs');
const {exec} = require("child_process");

const db = new sqlite3.Database('gold_backend/slingshot_api/api/tv/econ_live.db', (err) => {
  // console.log(fs.existsSync('../database/all_cn_futures.db'))
  if (err) {
    console.error('Error opening database:', err.message);
  } else {
    console.log('Connected to the SQLite database.');
  }
});

function get_econ_indicators(callback) {
  const db_loc = __dirname.toString().replace('\\express_service', '\\slingshot_api\\api\\tv')
  exec('python world_economy.py', {cwd: db_loc}, (error, stdout, stderr) => {
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
      const countries = ['US', 'CN', 'EU', 'JP', 'DE', 'GB', 'FR', 'RU', 'CA', 'IT', 'AU'];
      const indicators = ['GDP', 'POP', 'GDPYY', 'INTR', 'IRYY', 'UR', 'CAG', 'GDG'];

      const response = {};
      response['countries'] = countries;
      response['indicators'] = indicators;

      // Initialize response object for each country
      countries.forEach(country => {
        response[country] = {};
        indicators.forEach(indicator => {
          response[country][indicator] = {}
        })
      });

      rows.forEach((element) => {
        const country = element['field'].slice(0, 2);
        const indicator = element['field'].slice(2, );
        response[country][indicator] = {"value": element['value'], "change": element['change']};
      });
      callback(response)
    }
  })
  })
}

module.exports = {get_econ_indicators};