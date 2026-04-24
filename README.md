# Mapathon3rd Project

An interactive Mapbox-based presentation on Taiwan contingency and Japan's energy security.

## Quick Start

### Local Development

1. **Get a Mapbox Token:**
   - Sign up at https://www.mapbox.com/
   - Create a new token in Account > Tokens
   
2. **Update config.js:**
   - Open `config.js`
   - Replace `'YOUR_MAPBOX_ACCESS_TOKEN'` with your token:
   ```javascript
   const MAPBOX_ACCESS_TOKEN = 'pk.eyJ1IjoieW91cnVzZXJuYW1lIiwiYSI6ImNleW91cnRva2VuIn0...';
   ```

3. **Open in Browser:**
   - Open `index.html` in your web browser
   - Navigate through slides with ← and → buttons

### GitHub Pages Deployment

1. **Push to GitHub:**
   ```bash
   git push origin master
   ```

2. **Configure GitHub Secrets:**
   - Go to Settings > Secrets and variables > Actions
   - Create a new secret named `MAPBOX_ACCESS_TOKEN`
   - Paste your Mapbox token as the value

3. **Enable GitHub Pages:**
   - Go to Settings > Pages
   - Select "GitHub Actions" as the deployment source

4. **Automatic Deployment:**
   - The GitHub Actions workflow will automatically:
     - Generate `config.js` from the secret
     - Deploy the site to GitHub Pages
   - Your site will be live at `https://<your-username>.github.io/mapathon3rd`

## Project Features

- Interactive 7-slide presentation on Taiwan contingency and energy security
- Mapbox GL JS for map visualization
- Display of current oil shipping routes and alternative routes
- US military base locations in Japan
- Multi-language support (Japanese & English)
- Previous/Next slide navigation

## File Structure

```
mapathon3rd/
├── index.html              # Main presentation file
├── config.js               # Mapbox token (ignored by git)
├── config.example.js       # Template for config.js
├── .env                    # Local environment file (ignored by git)
├── .github/workflows/      # GitHub Actions for deployment
│   └── deploy.yml          # Auto-deploy workflow
├── geocode.py              # Script to convert addresses to coordinates
├── sekiyu.geojson          # Oil route data
├── ukai.geojson            # Alternative route data
├── us_bases_with_coords.csv # US military bases data
└── README.md               # This file
```

## Data Sources

- US Military Bases: https://www.e-stat.go.jp/stat-search/files?page=1&layout=datalist&toukei=00700011&kikan=00700&tstat=000001149526&cycle=0&tclass1=000001241996&tclass2val=0
- Shipping Routes: https://business.nikkei.com/atcl/gen/19/00530/012600005/

## Development Notes

- `config.js` contains your Mapbox token and is ignored by git
- `.env` file is local-only and not committed
- GitHub Actions automatically generates `config.js` during deployment using the secret
- The `.github/workflows/deploy.yml` orchestrates this process

## License

Project for educational purposes.
