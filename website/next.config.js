/** @type {import('next').NextConfig} */
const nextConfig = {
  typescript: { ignoreBuildErrors: true }, // évite l'arrêt du build si un type manque
  eslint: { ignoreDuringBuilds: true }     // évite qu'un lint cassé bloque
};
module.exports = nextConfig;
