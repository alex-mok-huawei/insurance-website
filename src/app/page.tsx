export default function Home() {
  return (
    <div className="min-h-screen">
      {/* Navbar */}
      <nav className="flex items-center justify-between px-8 py-4 bg-white shadow-sm sticky top-0 z-50">
        <div className="flex items-center gap-2">
          <svg className="w-8 h-8 text-blue-600" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2L3 7v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V7l-9-5z"/></svg>
          <span className="text-2xl font-bold text-blue-800">SafeGuard</span>
          <span className="text-xs text-blue-600 tracking-widest">INSURANCE</span>
        </div>
        <div className="hidden md:flex gap-8 text-gray-600 font-medium">
          <a href="#services" className="hover:text-blue-600 transition">Services</a>
          <a href="#about" className="hover:text-blue-600 transition">About</a>
          <a href="#testimonials" className="hover:text-blue-600 transition">Testimonials</a>
          <a href="#contact" className="hover:text-blue-600 transition">Contact</a>
        </div>
        <a href="#contact" className="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition font-medium">Get Quote</a>
      </nav>

      {/* Hero */}
      <section className="bg-gradient-to-r from-blue-900 to-blue-700 text-white py-24 px-8">
        <div className="max-w-6xl mx-auto">
          <h1 className="text-5xl md:text-6xl font-bold mb-6 leading-tight">Protecting What<br/>Matters Most</h1>
          <p className="text-xl mb-8 text-blue-100 max-w-2xl">Comprehensive insurance solutions for life, health, auto, and home. Peace of mind starts here.</p>
          <div className="flex gap-4 flex-wrap">
            <a href="#contact" className="bg-amber-500 text-white px-8 py-3 rounded-lg font-semibold hover:bg-amber-600 transition">Get Free Quote</a>
            <a href="#services" className="border-2 border-white text-white px-8 py-3 rounded-lg font-semibold hover:bg-white/10 transition">Our Services</a>
          </div>
        </div>
      </section>

      {/* Stats */}
      <section className="bg-white py-12 px-8 border-b">
        <div className="max-w-6xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
          <div><p className="text-4xl font-bold text-blue-800">500K+</p><p className="text-gray-500">Clients Protected</p></div>
          <div><p className="text-4xl font-bold text-blue-800">98%</p><p className="text-gray-500">Claims Approved</p></div>
          <div><p className="text-4xl font-bold text-blue-800">25+</p><p className="text-gray-500">Years Experience</p></div>
          <div><p className="text-4xl font-bold text-blue-800">24/7</p><p className="text-gray-500">Customer Support</p></div>
        </div>
      </section>
      {/* Services */}
      <section id="services" className="py-20 px-8 bg-gray-50">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-3xl font-bold text-center mb-4 text-gray-900">Our Insurance Services</h2>
          <p className="text-center text-gray-500 mb-12 max-w-2xl mx-auto">We offer a wide range of insurance products tailored to meet your unique needs.</p>
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            <div className="bg-white p-8 rounded-xl shadow-sm hover:shadow-md transition border border-gray-100">
              <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center mb-4 text-blue-600 text-2xl">&#9829;</div>
              <h3 className="text-xl font-semibold mb-2">Life Insurance</h3>
              <p className="text-gray-500">Protect your family financial future with comprehensive life coverage plans.</p>
            </div>
            <div className="bg-white p-8 rounded-xl shadow-sm hover:shadow-md transition border border-gray-100">
              <div className="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center mb-4 text-green-600 text-2xl">&#9764;</div>
              <h3 className="text-xl font-semibold mb-2">Health Insurance</h3>
              <p className="text-gray-500">Access quality healthcare with our extensive health insurance coverage options.</p>
            </div>
            <div className="bg-white p-8 rounded-xl shadow-sm hover:shadow-md transition border border-gray-100">
              <div className="w-12 h-12 bg-amber-100 rounded-lg flex items-center justify-center mb-4 text-amber-600 text-2xl">&#9731;</div>
              <h3 className="text-xl font-semibold mb-2">Auto Insurance</h3>
              <p className="text-gray-500">Drive with confidence knowing your vehicle is protected against any eventuality.</p>
            </div>
            <div className="bg-white p-8 rounded-xl shadow-sm hover:shadow-md transition border border-gray-100">
              <div className="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center mb-4 text-purple-600 text-2xl">&#8962;</div>
              <h3 className="text-xl font-semibold mb-2">Home Insurance</h3>
              <p className="text-gray-500">Safeguard your home and belongings with our comprehensive property coverage.</p>
            </div>
          </div>
        </div>
      </section>

      {/* About */}
      <section id="about" className="py-20 px-8 bg-white">
        <div className="max-w-6xl mx-auto grid md:grid-cols-2 gap-12 items-center">
          <div>
            <h2 className="text-3xl font-bold mb-6 text-gray-900">Why Choose SafeGuard?</h2>
            <p className="text-gray-500 mb-6">With over 25 years of experience, SafeGuard Insurance has been a trusted partner for families and businesses across the nation. Our commitment to excellence and customer-first approach sets us apart.</p>
            <ul className="space-y-4">
              <li className="flex items-start gap-3"><span className="text-green-500 text-xl mt-0.5">&#10003;</span><span className="text-gray-600">Fast and hassle-free claims processing</span></li>
              <li className="flex items-start gap-3"><span className="text-green-500 text-xl mt-0.5">&#10003;</span><span className="text-gray-600">Dedicated personal insurance advisor</span></li>
              <li className="flex items-start gap-3"><span className="text-green-500 text-xl mt-0.5">&#10003;</span><span className="text-gray-600">Flexible plans that grow with you</span></li>
              <li className="flex items-start gap-3"><span className="text-green-500 text-xl mt-0.5">&#10003;</span><span className="text-gray-600">24/7 customer support and assistance</span></li>
            </ul>
          </div>
          <div className="bg-gradient-to-br from-blue-100 to-blue-50 rounded-2xl p-12 text-center">
            <div className="text-6xl mb-4">&#128737;</div>
            <h3 className="text-2xl font-bold text-blue-800 mb-2">Trusted by 500,000+ Clients</h3>
            <p className="text-blue-600">Your protection is our priority</p>
          </div>
        </div>
      </section>

      {/* Testimonials */}
      <section id="testimonials" className="py-20 px-8 bg-gray-50">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-3xl font-bold text-center mb-4 text-gray-900">What Our Clients Say</h2>
          <p className="text-center text-gray-500 mb-12">Hear from our satisfied policyholders</p>
          <div className="grid md:grid-cols-3 gap-8">
            <div className="bg-white p-8 rounded-xl shadow-sm border border-gray-100">
              <div className="text-amber-400 text-xl mb-4">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
              <p className="text-gray-600 mb-6">SafeGuard made the claims process so easy. After my accident, they were there every step of the way. Truly exceptional service!</p>
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 bg-blue-200 rounded-full flex items-center justify-center text-blue-700 font-bold">S</div>
                <div><p className="font-semibold text-gray-900">Sarah Johnson</p><p className="text-sm text-gray-500">Auto Insurance Client</p></div>
              </div>
            </div>
            <div className="bg-white p-8 rounded-xl shadow-sm border border-gray-100">
              <div className="text-amber-400 text-xl mb-4">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
              <p className="text-gray-600 mb-6">I have been with SafeGuard for 10 years. Their health insurance plan saved my family during a medical emergency.</p>
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 bg-green-200 rounded-full flex items-center justify-center text-green-700 font-bold">M</div>
                <div><p className="font-semibold text-gray-900">Michael Chen</p><p className="text-sm text-gray-500">Health Insurance Client</p></div>
              </div>
            </div>
            <div className="bg-white p-8 rounded-xl shadow-sm border border-gray-100">
              <div className="text-amber-400 text-xl mb-4">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
              <p className="text-gray-600 mb-6">The best home insurance I have ever had. Competitive rates and outstanding customer support. Highly recommend!</p>
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 bg-purple-200 rounded-full flex items-center justify-center text-purple-700 font-bold">E</div>
                <div><p className="font-semibold text-gray-900">Emily Rodriguez</p><p className="text-sm text-gray-500">Home Insurance Client</p></div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Contact */}
      <section id="contact" className="py-20 px-8 bg-white">
        <div className="max-w-6xl mx-auto grid md:grid-cols-2 gap-12">
          <div>
            <h2 className="text-3xl font-bold mb-6 text-gray-900">Get Your Free Quote Today</h2>
            <p className="text-gray-500 mb-8">Fill out the form and one of our insurance advisors will get back to you within 24 hours with a personalized quote.</p>
            <div className="space-y-6">
              <div className="flex items-center gap-4">
                <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center text-blue-600 text-xl">&#9742;</div>
                <div><p className="font-semibold text-gray-900">Call Us</p><p className="text-gray-500">1-800-SAFE-GUARD</p></div>
              </div>
              <div className="flex items-center gap-4">
                <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center text-blue-600 text-xl">&#9993;</div>
                <div><p className="font-semibold text-gray-900">Email Us</p><p className="text-gray-500">info@safeguard-insurance.com</p></div>
              </div>
              <div className="flex items-center gap-4">
                <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center text-blue-600 text-xl">&#9873;</div>
                <div><p className="font-semibold text-gray-900">Visit Us</p><p className="text-gray-500">123 Insurance Blvd, Suite 500</p></div>
              </div>
            </div>
          </div>
          <form className="bg-gray-50 p-8 rounded-xl space-y-4">
            <input type="text" placeholder="Full Name" className="w-full px-4 py-3 rounded-lg border border-gray-200 focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none" />
            <input type="email" placeholder="Email Address" className="w-full px-4 py-3 rounded-lg border border-gray-200 focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none" />
            <input type="tel" placeholder="Phone Number" className="w-full px-4 py-3 rounded-lg border border-gray-200 focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none" />
            <select className="w-full px-4 py-3 rounded-lg border border-gray-200 focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none text-gray-500">
              <option>Select Insurance Type</option>
              <option>Life Insurance</option>
              <option>Health Insurance</option>
              <option>Auto Insurance</option>
              <option>Home Insurance</option>
            </select>
            <textarea placeholder="Your Message" rows={4} className="w-full px-4 py-3 rounded-lg border border-gray-200 focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none"></textarea>
            <button type="button" className="w-full bg-blue-600 text-white py-3 rounded-lg font-semibold hover:bg-blue-700 transition">Get My Free Quote</button>
          </form>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-900 text-gray-300 py-12 px-8">
        <div className="max-w-6xl mx-auto grid md:grid-cols-4 gap-8">
          <div>
            <div className="flex items-center gap-2 mb-4">
              <svg className="w-6 h-6 text-blue-400" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2L3 7v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V7l-9-5z"/></svg>
              <span className="text-xl font-bold text-white">SafeGuard</span>
            </div>
            <p className="text-sm">Protecting families and businesses for over 25 years with reliable insurance solutions.</p>
          </div>
          <div>
            <h4 className="font-semibold text-white mb-4">Services</h4>
            <ul className="space-y-2 text-sm">
              <li><a href="#services" className="hover:text-white transition">Life Insurance</a></li>
              <li><a href="#services" className="hover:text-white transition">Health Insurance</a></li>
              <li><a href="#services" className="hover:text-white transition">Auto Insurance</a></li>
              <li><a href="#services" className="hover:text-white transition">Home Insurance</a></li>
            </ul>
          </div>
          <div>
            <h4 className="font-semibold text-white mb-4">Company</h4>
            <ul className="space-y-2 text-sm">
              <li><a href="#about" className="hover:text-white transition">About Us</a></li>
              <li><a href="#testimonials" className="hover:text-white transition">Testimonials</a></li>
              <li><a href="#contact" className="hover:text-white transition">Contact</a></li>
              <li><a href="#" className="hover:text-white transition">Careers</a></li>
            </ul>
          </div>
          <div>
            <h4 className="font-semibold text-white mb-4">Legal</h4>
            <ul className="space-y-2 text-sm">
              <li><a href="#" className="hover:text-white transition">Privacy Policy</a></li>
              <li><a href="#" className="hover:text-white transition">Terms of Service</a></li>
              <li><a href="#" className="hover:text-white transition">Licenses</a></li>
              <li><a href="#" className="hover:text-white transition">Disclosures</a></li>
            </ul>
          </div>
        </div>
        <div className="max-w-6xl mx-auto mt-8 pt-8 border-t border-gray-700 text-center text-sm">
          <p>&copy; 2025 SafeGuard Insurance. All rights reserved.</p>
        </div>
      </footer>
    </div>
  );
}
