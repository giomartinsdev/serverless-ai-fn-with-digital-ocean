# Serverless AI Functions with DigitalOcean

This project demonstrates how to deploy AI inference functions to DigitalOcean's Serverless platform using Hugging Face models.

## Setup

1. Install doctl: `brew install doctl`
2. Connect to your DigitalOcean account: `doctl serverless connect`
3. Set your API token: `export do-token='your-token-here'`

## Deployment

```bash
doctl serverless deploy . --remote-build
```

## Usage

```bash
doctl serverless functions invoke ai/hf-inference -p prompt="Your prompt here"
```

## Environment Variables

Copy `.env.example` to `.env` and add your DigitalOcean API token:

```bash
cp packages/ai/hf-inference/.env.example packages/ai/hf-inference/.env
```

Then edit the `.env` file and add your token.
