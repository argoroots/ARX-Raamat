const https = require('https')


const postToPlausible = async (postData, Ip) => {
    return new Promise((resolve, reject) => {
        const options = {
            hostname: 'plausible.io',
            path: '/api/event',
            method: 'POST',
            headers: {
                'Authorization': 'Basic ' + Buffer.from('anystring:' + process.env.PLAUSIBLE_KEY).toString('base64'),
                'Content-Type': 'application/json',
                'X-Forwarded-For': Ip
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
        screen_width: 1900,
        props: {
            Library: event.queryStringParameters.Asutus_Nimi,
            Version: event.queryStringParameters.Programm_Versioon
        }
    }, event.headers['client-ip'])

    console.log(JSON.stringify(event, null, 2))
    console.log(JSON.stringify(event.queryStringParameters, null, 2))

    return {
        statusCode: 200,
        body: 'ARX-Raamat 7.0.150'
    }
}
