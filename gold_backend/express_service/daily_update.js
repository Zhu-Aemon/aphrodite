const exec = require('child_process').exec;

function data_update(symbol, callback) {
    try {
        const project_loc = __dirname.toString().replace('\\express_service\\daily_update.js', '\\python_service')
        exec('python CN_commodity.py', {cwd: project_loc})
        callback([])
    } catch (error) {
        console.log(error)
        callback([])
    }
}

module.exports = {data_update}