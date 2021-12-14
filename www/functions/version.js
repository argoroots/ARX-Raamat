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
                resolve(JSON.parse(body))
            })
        })

        request.on('error', reject)
        request.write(JSON.stringify(postData))
        request.end()
    })
}


exports.handler = async (event) => {
    const result = await postToMailChimp({
        domain: 'arx.ee',
        name: 'Version',
        url: 'app://localhost/versioon',
        props: {}
    })

    return {
        statusCode: 200,
        headers: {
            'Access-Control-Allow-Origin': '*'
        },
        body: JSON.stringify(event)
    }
}
