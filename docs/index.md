<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HarmoFinder User Documentation</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
        }
        .content-section {
            scroll-margin-top: 4rem;
        }
        .prose h1, .prose h2, .prose h3 {
            color: #1e3a8a;
            font-weight: 700;
        }
        .prose h1 {
            border-bottom: 2px solid #e5e7eb;
            padding-bottom: 0.5rem;
        }
        .prose h2 {
            border-bottom: 1px solid #e5e7eb;
            padding-bottom: 0.5rem;
        }
        .prose code {
            background-color: #eef2ff;
            color: #4338ca;
            padding: 0.2rem 0.4rem;
            border-radius: 0.25rem;
            font-weight: 600;
        }
        .prose a {
            color: #2563eb;
            text-decoration: none;
        }
        .prose a:hover {
            text-decoration: underline;
        }
        .sidebar-link {
            display: block;
            padding: 0.5rem 1rem;
            border-left: 3px solid transparent;
            color: #d1d5db;
            font-weight: 500;
            transition: all 0.2s ease-in-out;
        }
        .sidebar-link:hover {
            background-color: #374151;
            color: #ffffff;
            border-left-color: #3b82f6;
        }
        .sidebar-link.active {
            background-color: #1f2937;
            color: #ffffff;
            border-left-color: #3b82f6;
        }
        .sidebar-sub-link {
            padding-left: 2rem;
            font-size: 0.875rem;
        }
    </style>
</head>
<body class="bg-gray-100">

    <div class="flex flex-col md:flex-row min-h-screen">
        <!-- Sidebar -->
        <nav class="w-full md:w-64 bg-gray-800 text-white flex-shrink-0">
            <div class="p-4">
                <h2 class="text-xl font-bold text-white">HarmoFinder Docs</h2>
            </div>
            <div class="sticky top-0">
                <a href="#welcome-login" class="sidebar-link">Welcome & Login</a>
                <a href="#dashboard" class="sidebar-link">Your Dashboard</a>
                <a href="#signals" class="sidebar-link">Our Signals</a>
                <a href="#alpha" class="sidebar-link">Our "Alpha"</a>
                <a href="#trade-management" class="sidebar-link">Smart Trade Management</a>
                <a href="#market-indicators" class="sidebar-link">Proprietary Indicators</a>
                <a href="#account-management" class="sidebar-link">Account Management</a>
            </div>
        </nav>

        <!-- Main Content -->
        <main class="flex-1 p-6 md:p-10">
            <div class="prose max-w-none">

                <section id="welcome-login" class="content-section">
                    <h1>📚 HarmoFinder User Documentation</h1>

                    <h2>1. Welcome & Login</h2>
                    <p>Welcome to HarmoFinder. To access the platform, we offer several secure login methods designed to match your preferences for privacy and simplicity.</p>
                    <h3>Sign-In with Ethereum (SIWE)</h3>
                    <p><strong>Who is it for?</strong> The "crypto-native" option, ideal for users who prioritize pseudonymity and security.</p>
                    <p><strong>How it works:</strong> Use your wallet (e.g., MetaMask, Trust Wallet) to sign a message. You share no email, no password. Your wallet is your identity on our platform.</p>
                    <h3>Social Login (Discord & Twitter/X)</h3>
                    <p><strong>Who is it for?</strong> For users who want a fast, convenient login.</p>
                    <p><strong>How it works:</strong> Use your Discord or X account to log in with one click. These platforms are at the heart of the Web3 ecosystem, and we offer them as practical, "crypto-aligned" alternatives.</p>
                </section>

                <section id="dashboard" class="content-section">
                    <h2>2. Your Dashboard (The indice_frontend)</h2>
                    <p>Your dashboard is your command center. It's where you visualize the bot's work and track your performance.</p>
                    <ul>
                        <li><strong>Active Signals View:</strong> See all harmonic patterns the bot has detected that are currently being evaluated or are in an active trade.</li>
                        <li><strong>Trade History:</strong> Analyze all past trades (wins, losses, invalidations) to understand performance and refine your strategy.</li>
                        <li><strong>Performance Dashboard:</strong> Track your account's P&L, Win Rate, and other key performance metrics with clear visualizations.</li>
                    </ul>
                </section>

                <section id="signals" class="content-section">
                    <h2>3. Our Signals: Pattern Detection</h2>
                    <p>HarmoFinder doesn't just follow trends; it identifies complex price structures that predict market reversals with a high degree of probability.</p>
                    <h3>Classic Harmonic Patterns (Standard Tier)</h3>
                    <p><strong>What is it?</strong> Our core engine constantly scans the market for well-known XABCD patterns like the Gartley, Bat, Butterfly, and Cypher.</p>
                    <p><strong>How it works?</strong> The bot uses a ZigZag algorithm to identify significant pivot points (X, A, B, C) and checks if they adhere to the specific Fibonacci ratios that define each pattern.</p>
                    <h3>Advanced Patterns (GNN) (Expert/Quant Tier)</h3>
                    <p><strong>What is it?</strong> This is our most advanced technology. Classic patterns are rigid; our AI (a Graph Neural Network, or GNN) is trained to recognize more subtle and complex price structures that don't fit a textbook model but have historically shown a high probability of success.</p>
                    <p><strong>How it works?</strong> We transform price structures into "graphs" that our AI analyzes, allowing it to find opportunities that traditional scanners miss entirely.</p>
                </section>

                <section id="alpha" class="content-section">
                    <h2>4. Our "Alpha": Confluence Filters</h2>
                    <p>A pattern alone is a good start. A pattern validated by advanced market data is a high-conviction signal. This is our secret sauce for filtering out the noise.</p>
                    <h3>The Confidence Score (Pro/Quant Tier)</h3>
                    <p><strong>What is it?</strong> Your at-a-glance quality indicator for every signal. It tells you if the "smart money" and market sentiment align with the pattern.</p>
                    <p><strong>How it works?</strong> This score (from 0 to 100) is an aggregate of two key derivative market metrics:</p>
                    <ul>
                        <li><strong>Open Interest (OI):</strong> We analyze OI momentum to see if new capital is flowing in to support the move.</li>
                        <li><strong>Funding Rates (FR):</strong> We analyze funding rates to measure market sentiment (greed vs. fear).</li>
                    </ul>
                    <p><strong>Why it matters:</strong> A high score means capital flows and market sentiment confirm the pattern. This score is rigorously backtested to improve the Win Rate and Profit Factor.</p>
                    <h3>The "Liquidity Magnet" Score (Quant Tier)</h3>
                    <p><strong>What is it?</strong> Our most powerful filter. It checks if your pattern's entry zone (the PRZ) is sitting exactly on top of a "wall" of pending liquidations.</p>
                    <p><strong>How it works?</strong> We use Coinglass "Liquidation Maps". Our bot calculates a score (from 0.0 to 1.0) that measures the density of potential liquidations within the PRZ compared to the surrounding area.</p>
                    <p><strong>Why it matters:</strong> A high score (e.g., 0.8) means 80% of all nearby liquidity is concentrated in your entry zone. The pattern isn't just pointing to a technical level; it's pointing to the "fuel" for an imminent squeeze.</p>
                    <h3>Gann Time Confluence (Pro/Quant Tier)</h3>
                    <p><strong>What is it?</strong> Price is only half of the equation; time is the other half. This filter checks if a pattern is completing at a mathematically significant time.</p>
                    <p><strong>How it works?</strong> The bot calculates Gann "Time Reversal Zones" (TRZ) , based on the time cycles from the pattern's X, A, B, and C points.</p>
                    <p><strong>Why it matters:</strong> A signal forming in both a price PRZ and a time TRZ is a very high-probability setup. The bot even applies a leverage bonus for these "time-confluent" trades.</p>
                    <h3>Standard Confluence Filters (All Tiers)</h3>
                    <p>All our signals are also validated against a checklist of standard technical indicators, including RSI Divergence, MACD, Volume Profile (POC/VA), VWAP, and higher-timeframe trend alignment.</p>
                </section>

                <section id="trade-management" class="content-section">
                    <h2>5. Smart Trade Management: The Bot's Brain</h2>
                    <p>Our bot is not a simple alert service. It is an active trade manager that adapts to market conditions after a position is opened.</p>
                    <h3>Dynamic Entries</h3>
                    <p>The bot doesn't buy blindly. It waits for specific confirmations, such as a "15m Retest" of the zone, a "Near True Level" entry (the ideal Fibonacci ratio), or a "Near SL" entry (optimal risk/reward).</p>
                    <h3>Adaptive Partial Exits (Pro/Quant Tier)</h3>
                    <p>The bot reacts to real-time information:</p>
                    <ul>
                        <li><strong>MACD Confluence Failure:</strong> If the trade is open but MACD fails to confirm after the PRZ exit, the bot closes 50% of the position to reduce risk.</li>
                        <li><strong>"True Fib" PRZ Exit:</strong> If you entered on a perfect Fibonacci level, the bot secures 30% in profit as soon as the price exits the entry zone.</li>
                    </ul>
                    <h3>Dynamic Stop-Loss</h3>
                    <ul>
                        <li><strong>ATR Trailing Stop:</strong> Once in profit, the bot can activate an ATR (Average True Range) Trailing Stop, allowing it to lock in gains while giving the trade room to run.</li>
                        <li><strong>Candle Rejection Exit:</strong> If the bot detects a strong rejection candle (e.g., a long wick) near the SL, it can close the position before the SL is hit to prevent slippage.</li>
                    </ul>
                    <h3>Invalidation Handling (Quant Tier)</h3>
                    <p><strong>Invalidation & Reversal:</strong> What happens if a trade hits its Stop-Loss? The bot doesn't just take the loss. It considers the pattern "invalidated" and automatically opens a trade in the opposite direction, trading on the assumption that the pattern's failure is, itself, a strong signal.</p>
                    <p><strong>Double Invalidation:</strong> If the reversed trade also hits its SL, the bot closes the position for good. This is our "circuit breaker" for that pattern.</p>
                    <h3>Hedging (Quant Tier)</h3>
                    <p>When certain Take Profit (TP) levels are hit, the bot automatically opens a small hedge position in the opposite direction.</p>
                    <p><strong>Why?</strong> This allows you to lock in a portion of your gains while keeping your main position open to target higher objectives, all without emotion.</p>
                </section>

                <section id="market-indicators" class="content-section">
                    <h2>6. Proprietary Market Indicators</h2>
                    <p>Beyond trade signals, your dashboard gives you access to unique market gauges based on our internal research.</p>
                    <h3>The Weekend Risk Indicator</h3>
                    <p><strong>What is it?</strong> An indicator that alerts you when weekend trading conditions are particularly dangerous.</p>
                    <p><strong>Why?</strong> Our research (based on the "Weekend Risk Hedging Strategy" document) has shown that weekend liquidity is often "illusory". The "bid walls" you see can evaporate , leading to flash crashes and liquidation cascades. This indicator helps you decide whether to reduce exposure before the weekend.</p>
                    <h3>The Market "Squeeze Score"</h3>
                    <p><strong>What is it?</strong> An indicator that scans the market for "powder kegs" ready to explode.</p>
                    <p><strong>How it works?</strong> It identifies assets where a large number of traders are "trapped" on the wrong side (e.g., many shorts in a market that refuses to drop), combined with rising Open Interest and extreme Funding Rates.</p>
                    <p><strong>Why?</strong> It helps you find high-volatility squeeze opportunities before they happen.</p>
                    <h3>The "Peak Sentiment" Indicator</h3>
                    <p><strong>What is it?</strong> A market "extreme greed" indicator.</p>
                    <p><strong>How it works?</strong> It triggers when Open Interest (leverage) and Funding Rates (greed) hit extreme historical highs at the same time.</p>
                    <p><strong>Why?</strong> It helps you know when it's time to take profits—not because of a technical signal, but because the market has become dangerously euphoric and a reversal is likely.</p>
                </section>

                <section id="account-management" class="content-section">
                    <h2>7. Account Management & Security</h2>
                    <h3>Customer Billing Portal</h3>
                    <p>Manage your subscription with full autonomy. Our secure customer portal (powered by Stripe) allows you to:</p>
                    <ul>
                        <li>Change your plan (e.g., upgrade from Pro to Quant).</li>
                        <li>Update your payment methods.</li>
                        <li>View and download your invoices.</li>
                    </ul>
                    <h3>Account Security</h3>
                    <p><strong>Single Session Policy:</strong> To protect your account, we enforce a "Force Logout" policy. We only allow one active session at a time. If you log in on a new device (like your phone), your previous session (on your laptop) will be logged out automatically.</p>
                    <h3>Terms of Use (Fair Use)</h3>
                    <p>To ensure a high-quality service and protect the value of our "Alpha" for all users, our terms of use explicitly forbid the reselling, scraping, or redistribution of our signals. This policy is essential for maintaining the integrity of the platform.</p>
                </section>

            </div>
        </main>
    </div>

    <script>
        document.addEventListener("DOMContentLoaded", () => {
            const sections = document.querySelectorAll(".content-section");
            const navLinks = document.querySelectorAll(".sidebar-link");

            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        navLinks.forEach(link => {
                            link.classList.remove("active");
                            if (link.getAttribute("href").substring(1) === entry.target.id) {
                                link.classList.add("active");
                            }
                        });
                    }
                });
            }, { rootMargin: "0px 0px -50% 0px", threshold: 0.1 });

            sections.forEach(section => {
                observer.observe(section);
            });

            navLinks.forEach(link => {
                link.addEventListener("click", (e) => {
                    e.preventDefault();
                    const targetId = e.currentTarget.getAttribute("href").substring(1);
                    document.getElementById(targetId).scrollIntoView({
                        behavior: "smooth",
                        block: "start"
                    });
                    history.pushState(null, null, `#${targetId}`);
                });
            });
        });
    </script>
</body>
</html>
