import pathlib

BASE = pathlib.Path(r"C:\Users\MSY\Desktop\insurance-website\src\app")

page = """export default function Home() {
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
"""
(BASE / "page.tsx").write_text(page.strip(), encoding="utf-8")
print("part1 done")
