<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HarmoFinder Bot Documentation</title>
    <!-- Load Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Use Inter font -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
        }
        /* Custom styles for ReadTheDoc look */
        .content-section {
            scroll-margin-top: 4rem; /* Offset for sticky header */
        }
        .prose h1, .prose h2, .prose h3 {
            color: #1e3a8a; /* Dark blue */
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
            background-color: #eef2ff; /* Light indigo */
            color: #4338ca; /* Indigo */
            padding: 0.2rem 0.4rem;
            border-radius: 0.25rem;
            font-weight: 600;
        }
        .prose a {
            color: #2563eb; /* Blue */
            text-decoration: none;
        }
        .prose a:hover {
            text-decoration: underline;
        }
        .sidebar-link {
            display: block;
            padding: 0.5rem 1rem;
            border-left: 3px solid transparent;
            color: #d1d5db; /* Gray 300 */
            font-weight: 500;
            transition: all 0.2s ease-in-out;
        }
        .sidebar-link:hover {
            background-color: #374151; /* Gray 700 */
            color: #ffffff;
            border-left-color: #3b82f6; /* Blue 500 */
        }
        .sidebar-link.active {
            background-color: #1f2937; /* Gray 800 */
            color: #ffffff;
            border-left-color: #3b82f6; /* Blue 500 */
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
            <!-- Sticky navigation for sidebar -->
            <div class="sticky top-0">
                <a href="#introduction" class="sidebar-link active">Introduction</a>
                <a href="#pattern-vs-signal" class="sidebar-link">Pattern vs. Signal</a>
                <a href="#confidence-score" class="sidebar-link">The Confidence Score</a>
                <a href="#score-components" class="sidebar-link">Scoring Components</a>
                <a href="#geometric-purity" class="sidebar-link sidebar-sub-link">- Geometric Purity</a>
                <a href="#market-confluence" class="sidebar-link sidebar-sub-link">- Market Confluence</a>
                <a href="#ai-context-score" class="sidebar-link sidebar-sub-link">- AI Context Score</a>
                <a href="#final-checks" class="sidebar-link">Final Entry Checks</a>
            </div>
        </nav>

        <!-- Main Content -->
        <main class="flex-1 p-6 md:p-10">
            <div class="prose max-w-none">

                <!-- Introduction Section -->
                <section id="introduction" class="content-section">
                    <h1>Introduction: How The Bot Works</h1>
                    <p>The HarmoFinder Bot is a sophisticated algorithmic trading system. Its primary purpose is to identify, validate, and execute high-probability trading opportunities based on harmonic chart patterns.</p>
                    <p>It's crucial to understand that the bot is not a simple signal generator. It is a multi-stage validation pipeline designed to filter out low-quality "noise" and only act on "A+" grade setups. The entire process can be broken down into three phases:</p>
                    <ol>
                        <li><strong>Detection (The "HarmoFinder"):</strong> The system scans hundreds of assets across multiple timeframes (4h, 1D, 3D) 24/7. Its goal is to identify the geometric structure of a "Detected Pattern" (e.g., a Gartley, Bat, or Deep Crab).</li>
                        <li><strong>Validation (The "Confidence Engine"):</strong> This is the core of the system. Every Detected Pattern is immediately passed to a scoring engine. This engine assigns a <strong>Confidence Score (1-10)</strong> based on the pattern's quality, its location on the chart, and the underlying market context.</li>
                        <li><strong>Execution (The "Trade Monitor"):</strong> Only patterns that achieve a high Confidence Score (e.g., 7/10 or higher) are promoted to a "Trade Signal." Before any order is placed, this signal must pass a final set of real-time filters for risk management and market regime.</li>
                    </ol>
                    <!-- Visual representation of the funnel -->
                    <div class="bg-gray-50 p-4 rounded-lg my-4 text-center">
                        <span class="font-bold text-lg text-gray-700">Detection</span>
                        <div class="text-5xl text-blue-600">↓</div>
                        <span class="font-bold text-lg text-gray-700">Validation (Confidence Score)</span>
                        <div class="text-5xl text-blue-600">↓</div>
                        <span class="font-bold text-lg text-gray-700">Execution (Final Checks)</span>
                    </div>
                </section>

                <!-- Pattern vs. Signal Section -->
                <section id="pattern-vs-signal" class="content-section">
                    <h2>Pattern vs. Signal: The Core Concept</h2>
                    <p>This is the most important distinction for stakeholders to understand. The bot separates "patterns" from "signals."</p>
                    
                    <h3>Detected Pattern</h3>
                    <p>A <strong>Detected Pattern</strong> is simply raw material. It is a geometric shape that the `harmofinder` service has identified. The system may detect hundreds of these per day. Most are low-quality, "sloppy" patterns and are immediately discarded by the scoring engine. A Detected Pattern is <em>not</em> an instruction to trade.</p>

                    <h3>Trade Signal</h3>
                    <p>A <strong>Trade Signal</strong> is a high-quality, validated opportunity. It is a Detected Pattern that has successfully passed through the entire validation pipeline and received a high <strong>Confidence Score</strong>. Only these "A+" grade setups are passed to the `monitor_trades` service for potential execution.</p>

                    <blockquote>
                        <p><strong>Analogy:</strong> A <strong>Detected Pattern</strong> is like identifying a cloud that *looks* like a rain cloud. A <strong>Trade Signal</strong> is that same cloud, *plus* a confirmed 20-degree drop in temperature, a 90% humidity reading, and a rising wind. We only act on the signal, not the shape.</p>
                    </blockquote>
                </section>

                <!-- Confidence Score Section -->
                <section id="confidence-score" class="content-section">
                    <h2>The Confidence Score (1-10)</h2>
                    <p>The Confidence Score is the final, aggregated grade (from 1 to 10) that the system assigns to a pattern *after* it has been detected. It answers one question: <strong>"What is the probability of this pattern succeeding right now, in the current market conditions?"</strong></p>
                    <ul>
                        <li><strong>Score 1-3:</strong> Very low quality. Ignored.</li>
                        <li><strong>Score 4-6:</strong> Average quality. Ignored.</li>
                        <li><strong>Score 7-10:</strong> High quality, validated "Trade Signal." Passed to the execution engine.</li>
                    </ul>
                    
                    <h3>How it Impacts the Trade</h3>
                    <p>The Confidence Score is the primary filter for the entire system. In the `monitor_trades` service, there is a hard filter called the <code>confidence_score_filter</code>. We configure a minimum threshold (e.g., <code>7</code>). Any pattern that does not meet this minimum score is automatically rejected and will never be traded.</p>
                </section>

                <!-- Scoring Components Section -->
                <section id="score-components" class="content-section">
                    <h2>Scoring Components: How the Score is Calculated</h2>
                    <p>The final 1-10 score is not just one number. It is an aggregation of several independent scores, each analyzing a different aspect of the trade. The final score is built like this:</p>
                    <p class="bg-gray-100 p-3 rounded-md"><code>Final Score (1-10) = (Base Score from Geometric Purity) + (Market Confluence Bonus) + (AI Context Bonus/Penalty)</code></p>
                </section>

                <!-- Geometric Purity Section -->
                <section id="geometric-purity" class="content-section">
                    <h3>1. Geometric Purity Score (The Base Score)</h3>
                    <p>This is the first and most fundamental score, calculated by the `harmofinder/scoring_engine.py`.</p>
                    <ul>
                        <li><strong>What it is:</strong> A score of the pattern's *technical perfection*.</li>
                        <li><strong>How it's calculated:</strong> It measures how closely the pattern's Fibonacci ratios (the X, A, B, C, and D points) match the "textbook perfect" definition of that pattern. For example, a perfect Gartley pattern has its B-point at exactly the 0.618 retracement of the XA leg. A pattern with a B-point at 0.617 will receive a much higher purity score than one at 0.590.</li>
                        <li><strong>Impact:</strong> This forms the base of the final score. A "sloppy" or geometrically "ugly" pattern will start with a low base score and is highly unlikely to ever become a Trade Signal.</li>
                    </ul>
                </section>

                <!-- Market Confluence Section -->
                <section id="market-confluence" class="content-section">
                    <h3>2. Market Confluence Score (The "Where")</h3>
                    <p>This score answers *where* on the chart the pattern is completing. A pattern that completes at a major support/resistance level is far more reliable.</p>
                    <ul>
                        <li><strong>What it is:</strong> A score measuring the pattern's alignment with high-volume structural levels.</li>
                        <li><strong>How it's calculated:</strong> The system's `scoring_engine.py` (specifically the <code>calculate_volume_profile_score</code> function) checks the pattern's entry price (the D-point) against the **Volume Profile** of the asset.</li>
                        <li><strong>Impact (Bonus System):</strong>
                            <ul>
                                <li><strong>High Bonus:</strong> Awarded if the D-point lands directly on the **Point of Control (POC)** (the highest-volume price level).</li>
                                <li><strong>Medium Bonus:</strong> Awarded if the D-point lands on the **Value Area High (VAH)** or **Value Area Low (VAL)**.</li>
                                <li><strong>No Bonus:</strong> Awarded if the pattern completes in a low-volume "dead zone."</li>
                            </ul>
                        </li>
                    </ul>
                </section>

                <!-- AI Context Score Section -->
                <section id="ai-context-score" class="content-section">
                    <h3>3. AI Context Score (The "When" / Exotic Alpha)</h3>
                    <p>This is our proprietary "secret sauce" and a key part of the "deep research" from the `masterplan.txt`. This score answers, "is *now* a good time for this pattern to succeed?"</p>
                    <ul>
                        <li><strong>What it is:</strong> A predictive score from an AI model (XGBoost) trained on our historical trade data (`trade_journal`).</li>
                        <li><strong>How it's trained:</strong> The `backtesting/train_model.py` script trained the model by analyzing thousands of past trades. It learned what "invisible" market conditions were present during winning trades versus losing trades.</li>
                        <li><strong>How it's calculated (Live):</strong> The `update_indices/update_confidence_score.py` script runs periodically. It feeds the *live* market context into the AI model, which generates a score. This score is then fed into the final Confidence Score calculation.</li>
                        <li><strong>Data Used (Exotic Alpha):</strong>
                            <ul>
                                <li><strong>Derivatives Data:</strong> Funding Rates, Open Interest, CVD, and Liquidation data.</li>
                                <li><strong>On-Chain Data:</strong> Exchange Netflows, MVRV (Market Value to Realized Value), and Whale Accumulation.</li>
                                <li><strong>Options Data:</strong> Put/Call Ratio.</li>
                            </ul>
                        </li>
                        <li><strong>Impact:</strong> This score acts as a powerful bonus or penalty. A geometrically perfect (Purity) pattern at a key level (Confluence) might *still* be rejected if the AI model detects that, for example, high funding rates and exchange inflows are strongly opposing the trade.</li>
                    </ul>
                </section>

                <!-- Final Checks Section -->
                <section id="final-checks" class="content-section">
                    <h2>Final Entry Checks: The Execution Gateway</h2>
                    <p>Even after a pattern receives a high Confidence Score (e.g., 8/10) and becomes a "Trade Signal," the `monitor_trades` service performs a final list of checks before placing an order. A signal must pass *all* of these filters:</p>
                    <ol>
                        <li><strong>Confidence Score Filter:</strong> Is the score <code>&gt; 7</code> (or the configured threshold)?</li>
                        <li><strong>Market Regime Filter:</strong> Is the trade aligned with the broader market trend? The `market_regime_filter.py` will block a LONG trade, even if it has a high score, if the overall market is in a strong "Trending Down" regime.</li>
                        <li><strong>Contextual Filters:</strong> Are there any immediate "red flags"? The `funding_rate_filter.py` or `liquidation_context_filter.py` can stop a trade if market conditions are dangerously volatile or skewed.</li>
                        <li><strong>Risk Management Filter:</strong> Does the trade meet our internal Risk/Reward rules? The `calculation_logic.py` confirms the stop-loss is valid and calculates a safe position size based on our account equity.</li>
                    </ol>
                    <p class="font-bold text-lg text-blue-800">Only a signal that passes every single check in this entire funnel—from Detection to Purity to Confluence to AI Context to Final Filters—will result in an order being placed on the exchange.</p>
                </section>

            </div>
        </main>
    </div>

    <!-- Simple JS for active sidebar link -->
    <script>
        document.addEventListener("DOMContentLoaded", () => {
            const sections = document.querySelectorAll(".content-section");
            const navLinks = document.querySelectorAll(".sidebar-link");

            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        navLinks.forEach(link => {
                            link.classList.toggle("active", link.getAttribute("href").substring(1) === entry.target.id);
                        });
                    }
                });
            }, { rootMargin: "-50% 0px -50% 0px", threshold: 0.1 });

            sections.forEach(section => {
                observer.observe(section);
            });

            // Smooth scroll
            navLinks.forEach(link => {
                link.addEventListener("click", (e) => {
                    e.preventDefault();
                    const targetId = e.currentTarget.getAttribute("href").substring(1);
                    document.getElementById(targetId).scrollIntoView({
                        behavior: "smooth",
                        block: "start"
                    });
                    // Also update hash in URL
                    history.pushState(null, null, `#${targetId}`);
                });
            });
        });
    </script>
</body>
</html>
