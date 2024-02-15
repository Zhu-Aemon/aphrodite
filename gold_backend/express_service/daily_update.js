const exec = require('child_process').exec;

function data_update(symbol, callback) {
    try {
        const scriptLoc = __dirname.toString().replace('express_service', 'CN_commodity.py')
        const projLoc = scriptLoc.replace('\\CN_commodity.py', '')
        exec('python CN_commodity.py', {cwd: projLoc})
        callback([])
    } catch (error) {
        console.log(error)
        callback([])
    }
}

module.exports = {data_update}