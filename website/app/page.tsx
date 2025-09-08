export default function Home() {
  return (
    <section className="space-y-6">
      <h1 className="text-4xl font-bold tracking-tight">The .MEVE Standard</h1>
      <p className="text-lg text-gray-600 max-w-3xl">
        A simple file that proves existence, integrity, and authenticity.
        Free for personal use, API for professionals.
      </p>
      <div className="flex gap-3">
        <a href="/generate" className="rounded-lg bg-sky-600 px-4 py-2 text-white hover:bg-sky-700">Generate proof</a>
        <a href="/verify" className="rounded-lg border px-4 py-2 hover:bg-gray-100">Verify proof</a>
      </div>
      <p className="text-sm text-gray-500">
        No persistence: your files are processed in memory. Max size 25 MB.
      </p>
    </section>
  );
}
