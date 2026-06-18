import pathlib
BASE = pathlib.Path(r"C:\Users\MSY\Desktop\insurance-website\src\app")
existing = (BASE / "page.tsx").read_text(encoding="utf-8")
add = """
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
"""
(BASE / "page.tsx").write_text(existing + add, encoding="utf-8")
print("part5 done - page.tsx complete!")
