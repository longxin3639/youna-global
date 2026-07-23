// Speed Insights initialization for Youna Global
// This script loads Vercel Speed Insights for performance monitoring

import { injectSpeedInsights } from './speed-insights-lib.mjs';

// Initialize Speed Insights
injectSpeedInsights({
  debug: false // Set to true for development debugging
});
