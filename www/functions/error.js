const https = require('https')


const postToPlausible = async (postData) => {
    return new Promise((resolve, reject) => {
        const options = {
            hostname: 'plausible.io',
            path: '/api/event',
            method: 'POST',
            headers: {
                'Authorization': 'Basic ' + Buffer.from('anystring:' + process.env.PLAUSIBLE_KEY).toString('base64'),
                'Content-Type': 'application/json'
            }
        }

        const request = https.request(options, response => {
            var body = ''

            response.on('data', function (d) {
                body += d
            })

            response.on('end', function () {
                resolve(body)
            })
        })

        request.on('error', reject)
        request.write(JSON.stringify(postData))
        request.end()
    })
}


exports.handler = async (event) => {
    const result = await postToPlausible({
        domain: 'arx.ee',
        name: 'Error',
        url: 'app://localhost/error',
        props: {}
    })

    console.log(event)
    console.log(result)

    return {
        statusCode: 200,
        body: 'ARX-Raamat 7.0.150'
    }
}
