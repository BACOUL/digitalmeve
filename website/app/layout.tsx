import "./globals.css";

export const metadata = {
  title: "DigitalMeve — The .MEVE Standard",
  description: "Timestamp, hash & certify any document in seconds.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-gray-50 text-gray-900 antialiased">
        <header className="border-b bg-white">
          <nav className="mx-auto max-w-6xl flex items-center justify-between px-4 py-3">
            <a href="/" className="font-semibold text-xl">Digital<span className="text-sky-600">Meve</span></a>
            <div className="flex gap-4 text-sm">
              <a href="/generate" className="hover:text-sky-700">Generate</a>
              <a href="/verify" className="hover:text-sky-700">Verify</a>
              <a href="/docs" className="hover:text-sky-700">Docs</a>
              <a href="/pricing" className="hover:text-sky-700">Pricing</a>
              <a href="/contact" className="hover:text-sky-700">Contact</a>
            </div>
          </nav>
        </header>
        <main className="mx-auto max-w-6xl px-4 py-10">{children}</main>
      </body>
    </html>
  );
}
