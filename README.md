# Jayesh Luthra - Personal Landing Page

A minimalist, clean "under construction" landing page for [jayeshluthra.com](https://jayeshluthra.com). 

## Project Overview

This repository contains the front-end code and deployment utilities for a simple web interface featuring the text **"machines in making"** along with a modern, rounded-corner dot loading animation. The design uses a white theme with gray/black outlines and a Google font (Varela Round).

## File Structure

- `index.html`: The main HTML document containing the structure of the landing page.
- `style.css`: The CSS stylesheet that defines the typography, the centered minimalist layout, the double-character text style, and the custom dot loading animation.
- `deploy.py`: A Python script that utilizes the Vercel REST API to programmatically deploy the site's files directly to a Vercel project (`jayeshs-personal-site`).

## Deployment

The project can be deployed instantly to Vercel via the included Python rollout script.

1. Ensure you have Python installed.
2. Execute the deployment script:
   ```bash
   python3 deploy.py
   ```
3. If successful, the script will output the Vercel deployment URL.

## Local Development

To view the landing page locally, simply open the `index.html` file in any modern web browser. No local development server or build-step is required.