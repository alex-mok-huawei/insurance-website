import pathlib
BASE = pathlib.Path(r"C:\Users\MSY\Desktop\insurance-website\src\app")
existing = (BASE / "page.tsx").read_text(encoding="utf-8")
add = """
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
"""
(BASE / "page.tsx").write_text(existing + add, encoding="utf-8")
print("part3 done")
