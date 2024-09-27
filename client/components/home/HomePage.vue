<template>
  <div class="container">
    <!-- Hero Section -->
    <section class="hero-section">
      <h1 class="display-4">Welcome to WebDevLab</h1>
      <p class="lead">Your Partner for Web Development and Web3 Solutions</p>
      <a href="#contact" class="btn btn-primary btn-lg">Get in Touch</a>
    </section>

    <!-- Services Section -->
    <section id="services" class="services-section">
      <div class="container text-center">
        <h2 class="mb-5">Our Services</h2>
        <div class="row">
          <div class="col-md-4">
            <div class="card service-card">
              <div class="card-body">
                <h5 class="card-title">Web Development</h5>
                <p class="card-text">Custom websites, responsive design, and full-stack development to bring your ideas
                  to life.</p>
              </div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="card service-card">
              <div class="card-body">
                <h5 class="card-title">Web3 Solutions</h5>
                <p class="card-text">Build decentralized applications and integrate blockchain technology into your
                  business.</p>
              </div>
            </div>
          </div>
          <div class="col-md-4">
            <div class="card service-card">
              <div class="card-body">
                <h5 class="card-title">Consulting</h5>
                <p class="card-text">Expert advice on Web3, blockchain, and digital transformation strategies.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- YouTube Section -->
    <section class="youtube-section bg-light py-5">
      <div class="container text-center">
        <h2 class="mb-4">Check out our YouTube Channel</h2>
        <p class="lead">Learn more about Web Development and Web3 through our tutorials and insights.</p>
        <a href="https://www.youtube.com/@web-dev-lab" class="btn btn-danger btn-lg">Visit our YouTube Channel</a>
      </div>
    </section>

    <!-- Contact Us Section -->
    <section id="contact" class="contact-section py-5">
      <div class="container text-center">
        <h2 class="mb-5 display-6">Get in Touch</h2>
        <p class="lead text-muted">We’d love to hear from you! Whether you have a project in mind or just want to ask a
          question, reach out to us.</p>

        <!-- Contact Details -->
        <div class="row text-center mb-5">
          <div class="col-md-4 mb-4">
            <div class="p-4 border rounded shadow-sm bg-light">
              <i class="bi bi-envelope-fill fs-2 mb-3 text-primary"></i>
              <h5>Email</h5>
              <p class="text-muted"><a href="mailto:mdsamsuzzoha5222@gmail.com"
                  class="text-decoration-none text-dark">mdsamsuzzoha5222@gmail.com</a></p>
            </div>
          </div>
          <div class="col-md-4 mb-4">
            <div class="p-4 border rounded shadow-sm bg-light">
              <i class="bi bi-telephone-fill fs-2 mb-3 text-primary"></i>
              <h5>Phone</h5>
              <p class="text-muted"><a href="tel:+8801889171929" class="text-decoration-none text-dark">+8801889171929</a>
              </p>
            </div>
          </div>
          <div class="col-md-4 mb-4">
            <div class="p-4 border rounded shadow-sm bg-light">
              <i class="bi bi-geo-alt-fill fs-2 mb-3 text-primary"></i>
              <h5>Address</h5>
              <p class="text-muted">58-Gha, West Rajabazaar, Dhaka, Bangladesh</p>
            </div>
          </div>
        </div>

        <!-- Contact Form -->
        <div class="row">
          <div class="col-md-8 offset-md-2">
            <div class="p-4 border rounded shadow-lg bg-light">
              <h5 class="mb-4">Send Us a Message</h5>
              <form class="contact-form">
                <div class="mb-3">
                  <input type="text" class="form-control" placeholder="Your Name" required>
                </div>
                <div class="mb-3">
                  <input type="email" class="form-control" placeholder="Your Email" required>
                </div>
                <div class="mb-3">
                  <textarea class="form-control" rows="5" placeholder="Your Message" required></textarea>
                </div>
                <button type="submit" class="btn btn-primary btn-lg px-5">Send Message</button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </section>


    <!-- Footer -->
    <footer>
      <p>© 2024 WebDevLab | Web Development & Web3 Agency | <a href="mailto:mdsamsuzzoha5222@gmail.com"
          style="color: #fff;">mdsamsuzzoha5222@gmail.com</a> | 58-Gha, West Rajabazaar, Dhaka, Bangladesh</p>
    </footer>

  </div>
</template>

<script lang="ts" setup>

</script>


<style lang="scss">
body {
  font-family: 'Arial', sans-serif;
}

.hero-section {
  height: 50vh;
  background: linear-gradient(to right, #6a11cb, #2575fc);
  color: white;
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

.services-section,
.contact-section {
  padding: 60px 0;
}

.service-card {
  border: none;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s;
}

.service-card:hover {
  transform: translateY(-10px);
}

.contact-form input,
.contact-form textarea {
  border-radius: 0;
}

footer {
  background-color: #333;
  color: white;
  padding: 20px;
  text-align: center;
}

.btn-primary {
  background-color: #6a11cb;
  border-color: #6a11cb;
}
</style>
