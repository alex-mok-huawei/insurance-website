import pathlib
BASE = pathlib.Path(r"C:\Users\MSY\Desktop\insurance-website\src\app")
existing = (BASE / "page.tsx").read_text(encoding="utf-8")
add = """
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
"""
(BASE / "page.tsx").write_text(existing + add, encoding="utf-8")
print("part4 done")
