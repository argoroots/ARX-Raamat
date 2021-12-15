const https = require('https')


const postToPlausible = async (postData, ip) => {
    return new Promise((resolve, reject) => {
        const options = {
            hostname: 'plausible.io',
            path: '/api/event',
            method: 'POST',
            headers: {
                'Authorization': 'Basic ' + Buffer.from('anystring:' + process.env.PLAUSIBLE_KEY).toString('base64'),
                'Content-Type': 'application/json',
                'X-Forwarded-For': ip
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
    const ip = event.headers['x-nf-client-connection-ip'] || event.headers['x-bb-ip'] || event.headers['client-ip']
    const library = event.queryStringParameters.Asutus_Nimi
    const version = event.queryStringParameters.Programm_Versioon || event.queryStringParameters.Programm_VersiooniNr || event.queryStringParameters.voti_versioon

    const result = await postToPlausible({
        domain: 'arx.ee',
        name: 'App',
        url: event.path,
        screen_width: 1900,
        props: {
            Library: library,
            Version: version
        }
    }, ip)

    console.log(JSON.stringify(event.queryStringParameters, null, 2))

    return {
        statusCode: 200,
        body: 'ARX-Raamat 7.0.150'
    }
}
