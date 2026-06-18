import pathlib
BASE = pathlib.Path(r"C:\Users\MSY\Desktop\insurance-website\src\app")
existing = (BASE / "page.tsx").read_text(encoding="utf-8")
add = """
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
"""
(BASE / "page.tsx").write_text(existing + add, encoding="utf-8")
print("part2 done")
