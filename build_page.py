import pathlib
BASE = pathlib.Path(r"C:\Users\MSY\Desktop\insurance-website\src\app")
page = """export default function Home() {
  return (
    <div className="min-h-screen">
      <p>Hello</p>
    </div>
  );
}
"""
(BASE / "page.tsx").write_text(page, encoding="utf-8")
print("done")
