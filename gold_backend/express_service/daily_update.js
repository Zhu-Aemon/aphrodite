const exec = require('child_process').exec;

function data_update(symbol, callback) {
    try {
        const project_loc = __dirname.toString().replace('\\express_service', '\\python_service')
        console.log(project_loc)
        // exec('python CN_commodity.py', {cwd: project_loc}, (error, stdout, stderr) => {
        //     if (error) {
        //         console.error(`exec error: ${error}`);
        //         return;
        //     }
        //     console.log(`stdout: ${stdout}`);
        //     console.error(`stderr: ${stderr}`);
        // })
        // exec('python update_indicator.py', {cwd: project_loc}, (error, stdout, stderr) => {
        //     if (error) {
        //         console.error(`exec error: ${error}`);
        //         return;
        //     }
        //     console.log(`stdout: ${stdout}`);
        //     console.error(`stderr: ${stderr}`);
        // })
        // exec('python update_forex.py', {cwd: project_loc}, (error, stdout, stderr) => {
        //     if (error) {
        //         console.error(`exec error: ${error}`);
        //         return;
        //     }
        //     console.log(`stdout: ${stdout}`);
        //     console.error(`stderr: ${stderr}`);
        // })
        callback([])
    } catch (error) {
        console.log(error)
        callback([])
    }
}

module.exports = {data_update}