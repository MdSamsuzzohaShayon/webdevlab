import sgMail from '@sendgrid/mail'

// Load API key from environment variable
sgMail.setApiKey(process.env.SENDGRID_API_KEY as string)

export default defineEventHandler(async (event) => {
  const body = await readBody(event)

  try {
    const msg = {
      to: body.to, // recipient
      from: 'admin@webdevlab.org', // your authenticated domain
      subject: body.subject,
      text: body.message,
      html: `<p>${body.message}</p>`
    }

    await sgMail.send(msg)

    return { success: true, message: 'Email sent successfully!' }
  } catch (error: any) {
    console.error(error)
    return { success: false, message: 'Failed to send email', error }
  }
})


/*

curl -X POST http://localhost:3001/api/send-email   -H "Content-Type: application/json"   -d '{
    "to": "mdshayon0@gmail.com",
    "subject": "Test Email from SendGrid",
    "message": "This is a test email sent from Nuxt.js API using SendGrid!"
  }'

*/