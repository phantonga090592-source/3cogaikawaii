<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bí Ấn Lịch Sử Việt Nam - Game Giải Đố 6 Level</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Font Awesome icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;900&family=Montserrat:wght@400;600;700;800&family=Playfair+Display:ital,wght@0,700;1,600&display=swap" rel="stylesheet">

    <style>
        body {
            font-family: 'Montserrat', sans-serif;
            user-select: none;
            overflow-x: hidden;
            background-color: #0c0a09;
            color: #f3e5ab;
        }

        .font-title { font-family: 'Cinzel', serif; }
        .font-ancient { font-family: 'Playfair Display', serif; }

        .text-gold-gradient {
            background: linear-gradient(180deg, #fff3a1 0%, #f1a80a 50%, #945500 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            filter: drop-shadow(0px 4px 10px rgba(0, 0, 0, 0.9));
        }

        .btn-play {
            background: linear-gradient(135deg, #b91c1c 0%, #f59e0b 50%, #9a3412 100%);
            box-shadow: 0 0 25px rgba(245, 158, 11, 0.6), inset 0 0 10px rgba(255, 255, 255, 0.5);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .btn-play:hover {
            transform: scale(1.05);
            box-shadow: 0 0 40px rgba(245, 158, 11, 0.9), inset 0 0 15px rgba(255, 255, 255, 0.8);
        }
        .btn-play:active { transform: scale(0.98); }

        .ancient-border {
            border: 3px solid #d97706;
            outline: 2px solid #78350f;
            outline-offset: 3px;
            box-shadow: inset 0 0 50px rgba(0,0,0,0.85), 0 10px 35px rgba(0,0,0,0.9);
        }

        .level-card { transition: all 0.3s ease; }
        .level-card:hover:not(.locked) {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(217, 119, 6, 0.3);
        }

        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-8px); }
        }
        @keyframes pulse-glow {
            0%, 100% { opacity: 0.25; filter: blur(25px); }
            50% { opacity: 0.6; filter: blur(35px); }
        }
        @keyframes spin-slow {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }

        .animate-float { animation: float 5s ease-in-out infinite; }
        .animate-glow { animation: pulse-glow 4s ease-in-out infinite; }
        .animate-spin-slow { animation: spin-slow 80s linear infinite; }

        .modal-bg {
            background: rgba(12, 10, 9, 0.92);
            backdrop-filter: blur(8px);
        }

        #timerCircle {
            transition: stroke-dashoffset 1s linear, stroke 0.3s ease;
        }
        
        /* Custom scrollbar */
        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-track { background: #1c1917; }
        ::-webkit-scrollbar-thumb { background: #b45309; rounded: 4px; }
    </style>
</head>
<body class="min-h-screen flex flex-col justify-between relative bg-stone-950 overflow-x-hidden select-none">

    <!-- Background Canvas Particles -->
    <canvas id="particleCanvas" class="absolute inset-0 pointer-events-none z-0"></canvas>
    <div class="absolute inset-0 z-0 opacity-15 bg-[radial-gradient(#d97706_1px,transparent_1px)] [background-size:24px_24px]"></div>
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[500px] h-[500px] bg-amber-600/20 rounded-full animate-glow pointer-events-none z-0"></div>

    <!-- Rotating Drum Background Pattern -->
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[650px] h-[650px] md:w-[850px] md:h-[850px] opacity-10 pointer-events-none z-0 animate-spin-slow flex items-center justify-center">
        <svg viewBox="0 0 200 200" class="w-full h-full stroke-amber-400 fill-none" stroke-width="0.5">
            <circle cx="100" cy="100" r="95" stroke-dasharray="2,2"/>
            <circle cx="100" cy="100" r="85"/>
            <circle cx="100" cy="100" r="70" stroke-dasharray="4,2"/>
            <circle cx="100" cy="100" r="50"/>
            <polygon points="100,70 106,90 126,90 110,102 116,122 100,110 84,122 90,102 74,90 94,90" fill="currentColor" opacity="0.3"/>
        </svg>
    </div>

    <!-- HEADER / TOP BAR -->
    <header class="relative z-20 w-full p-4 md:p-5 flex justify-between items-center max-w-7xl mx-auto">
        <div onclick="returnToCover()" class="cursor-pointer flex items-center space-x-3 bg-stone-900/90 border border-amber-600/50 px-4 py-2 rounded-full shadow-lg backdrop-blur-md hover:border-amber-400 transition-colors">
            <i class="fa-solid fa-scroll text-amber-500 text-lg"></i>
            <span class="font-title text-xs md:text-sm tracking-widest text-amber-200 font-bold">ĐẠI VIỆT SỬ KÝ</span>
        </div>

        <div class="flex items-center space-x-3">
            <button id="btnSoundToggle" onclick="toggleSound()" title="Âm thanh" class="w-11 h-11 rounded-full bg-stone-900/90 border border-amber-600/60 text-amber-400 hover:text-amber-200 hover:border-amber-400 flex items-center justify-center transition-all shadow-lg hover:scale-105 active:scale-95">
                <i id="soundIcon" class="fa-solid fa-volume-high text-base"></i>
            </button>

            <!-- Settings Button (Top Right) -->
            <button onclick="openSettings()" title="Cài đặt" class="group relative w-11 h-11 rounded-full bg-gradient-to-br from-amber-700 to-stone-900 border-2 border-amber-500 text-amber-300 hover:text-white flex items-center justify-center transition-all shadow-xl hover:scale-110 active:scale-95">
                <i class="fa-solid fa-gear text-lg group-hover:rotate-90 transition-transform duration-500"></i>
            </button>
        </div>
    </header>

    <!-- SCREEN 1: LANDING / BÌA GAME MAIN MENU -->
    <main id="mainCover" class="relative z-10 flex-1 flex flex-col items-center justify-center px-4 py-6 text-center max-w-5xl mx-auto w-full">
        <div class="mb-2 flex items-center justify-center space-x-4 opacity-90">
            <div class="h-[2px] w-12 md:w-24 bg-gradient-to-r from-transparent to-amber-500"></div>
            <i class="fa-solid fa-crown text-amber-500 text-xl md:text-2xl animate-bounce"></i>
            <div class="h-[2px] w-12 md:w-24 bg-gradient-to-l from-transparent to-amber-500"></div>
        </div>

        <div class="space-y-3 mb-6 animate-float">
            <h2 class="text-amber-400 text-xs md:text-base font-semibold tracking-[0.3em] uppercase drop-shadow">Hành Trình Ngàn Năm Dựng Nước & Giữ Nước</h2>
            <h1 class="font-title text-3xl sm:text-5xl md:text-6xl font-black tracking-wider text-gold-gradient uppercase leading-tight">
                BÍ ẨN LỊCH SỬ<br/>VIỆT NAM
            </h1>
            <p class="font-ancient text-amber-200/90 italic text-sm sm:text-base max-w-xl mx-auto pt-1">
                "6 Màn chơi - 90 Câu hỏi thử thách - Chinh phục kho tàng tri thức dân tộc"
            </p>
        </div>

        <!-- Center Graphic Badge -->
        <div class="relative w-full max-w-md my-4 flex justify-center items-center">
            <div class="relative z-10 w-44 h-44 md:w-52 md:h-52 rounded-2xl bg-gradient-to-b from-amber-950/80 to-stone-950/90 border-2 border-amber-500/80 p-4 shadow-2xl flex flex-col items-center justify-center backdrop-blur-md">
                <div class="absolute inset-2 border border-amber-600/40 rounded-xl pointer-events-none"></div>
                <div class="relative text-amber-400 mb-2">
                    <i class="fa-solid fa-landmark text-5xl md:text-6xl drop-shadow-[0_0_15px_rgba(245,158,11,0.8)]"></i>
                </div>
                <div class="flex items-center space-x-2 text-xs font-semibold text-amber-300 bg-amber-950/80 px-3 py-1 rounded-full border border-amber-700/60 mt-2">
                    <i class="fa-solid fa-star text-amber-400"></i>
                    <span id="totalStarsCount">Tổng Sao: 0/18</span>
                </div>
            </div>
        </div>

        <!-- Start Play Button -->
        <div class="mt-4 mb-4 w-full flex flex-col items-center">
            <button onclick="goToLevelSelect()" class="btn-play px-10 py-4 md:px-12 md:py-4 rounded-full text-white font-title text-lg md:text-xl font-black tracking-widest flex items-center space-x-3 border-2 border-amber-300 cursor-pointer">
                <i class="fa-solid fa-play text-xl text-amber-200 animate-pulse"></i>
                <span>BẮT ĐẦU CHƠI</span>
                <i class="fa-solid fa-chevron-right text-base text-amber-200"></i>
            </button>
            <p class="text-xs text-amber-400/70 mt-3 font-medium tracking-wide">
                <i class="fa-solid fa-layer-group mr-1"></i> Khám phá 6 thời kỳ lịch sử từ Văn Lang đến Đổi Mới
            </p>
        </div>
    </main>

    <!-- SCREEN 2: LEVEL SELECTION SCREEN (6 LEVELS) -->
    <main id="levelSelectScreen" class="hidden relative z-10 flex-1 flex flex-col items-center justify-center px-4 py-6 max-w-6xl mx-auto w-full">
        <div class="text-center mb-6">
            <h2 class="font-title text-2xl md:text-3xl font-bold text-amber-300">CHỌN MÀN CHƠI</h2>
            <p class="text-xs md:text-sm text-amber-200/80 mt-1">Đạt ít nhất 1 sao (8/15 câu đúng) để mở khóa màn tiếp theo</p>
        </div>

        <div id="levelsGrid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5 w-full mb-8">
            <!-- 6 Dynamic Level Cards injected by JS -->
        </div>

        <button onclick="returnToCover()" class="px-6 py-2.5 rounded-full bg-stone-900 border border-amber-600/60 text-amber-300 hover:text-amber-100 hover:bg-amber-950 text-sm font-semibold flex items-center space-x-2 transition-all">
            <i class="fa-solid fa-house"></i>
            <span>Về Màn Hình Chính</span>
        </button>
    </main>

    <!-- SCREEN 3: GAMEPLAY QUIZ SCREEN -->
    <main id="gameScreen" class="hidden relative z-10 flex-1 flex flex-col items-center justify-center px-4 py-4 max-w-3xl mx-auto w-full">
        <div class="w-full bg-stone-900/95 border-2 border-amber-600 rounded-2xl p-5 md:p-6 shadow-2xl relative ancient-border">
            
            <!-- Quiz Top Info Bar -->
            <div class="flex justify-between items-center mb-3 pb-3 border-b border-amber-800/60">
                <div class="flex items-center space-x-2">
                    <span id="levelBadge" class="bg-amber-900/90 text-amber-300 text-xs font-bold px-3 py-1 rounded-full border border-amber-600">
                        LEVEL 1
                    </span>
                    <span id="qCounter" class="text-amber-200/90 text-xs font-semibold">
                        Câu 1/15
                    </span>
                </div>

                <!-- Timer Ring Widget -->
                <div class="relative flex items-center justify-center w-11 h-11">
                    <svg class="w-11 h-11 transform -rotate-90">
                        <circle cx="22" cy="22" r="17" stroke="#44403c" stroke-width="4" fill="none"/>
                        <circle id="timerCircle" cx="22" cy="22" r="17" stroke="#f59e0b" stroke-width="4" fill="none" stroke-dasharray="107" stroke-dashoffset="0"/>
                    </svg>
                    <span id="timerText" class="absolute text-xs font-bold text-amber-200">25</span>
                </div>

                <!-- Score & Streak -->
                <div class="text-right">
                    <div class="text-[10px] text-amber-400/80 uppercase font-semibold">Điểm số</div>
                    <div id="scoreText" class="text-base md:text-lg font-black text-amber-300">0</div>
                </div>
            </div>

            <!-- Combo streak notification -->
            <div id="streakBadge" class="hidden mb-2 text-center text-xs font-bold text-amber-400 bg-amber-950/60 py-1 px-3 rounded-full border border-amber-700/50">
                <i class="fa-solid fa-fire text-orange-500 mr-1 animate-bounce"></i> Combo x<span id="streakNum">2</span>! (+Bonus)
            </div>

            <!-- Question Box -->
            <div class="mb-5 text-center min-h-[85px] flex items-center justify-center px-2">
                <h3 id="questionText" class="font-ancient text-base md:text-lg text-amber-100 font-semibold leading-relaxed">
                    ...
                </h3>
            </div>

            <!-- Options Grid -->
            <div id="optionsGrid" class="grid grid-cols-1 md:grid-cols-2 gap-3 mb-4">
                <!-- 4 Options injected dynamically -->
            </div>

            <!-- Historical Explanation Box (Shows after answer) -->
            <div id="explanationBox" class="hidden mb-4 p-3 bg-stone-950/90 border border-amber-700/70 rounded-xl text-xs text-amber-200 leading-relaxed">
                <div class="font-bold text-amber-400 mb-1 flex items-center">
                    <i class="fa-solid fa-book-bookmark mr-1.5"></i> Kiến Thức Lịch Sử:
                </div>
                <p id="explanationText"></p>
            </div>

            <!-- Lifelines Power-ups Bar -->
            <div class="flex justify-between items-center pt-3 border-t border-amber-900/40">
                <div class="flex items-center space-x-2">
                    <button id="btnFifty" onclick="useFiftyFifty()" title="Loại 2 đáp án sai" class="px-3 py-1.5 rounded-lg bg-stone-800 border border-amber-700 text-amber-300 hover:bg-amber-900/60 text-xs font-bold flex items-center space-x-1 disabled:opacity-40 disabled:cursor-not-allowed transition-all">
                        <i class="fa-solid fa-percent text-amber-400"></i>
                        <span>50:50</span>
                    </button>
                    <button id="btnHint" onclick="useHint()" title="Xem gợi ý" class="px-3 py-1.5 rounded-lg bg-stone-800 border border-amber-700 text-amber-300 hover:bg-amber-900/60 text-xs font-bold flex items-center space-x-1 disabled:opacity-40 disabled:cursor-not-allowed transition-all">
                        <i class="fa-regular fa-lightbulb text-amber-400"></i>
                        <span>Gợi Ý</span>
                    </button>
                    <button id="btnAudience" onclick="useAudience()" title="Hỏi khán giả" class="px-3 py-1.5 rounded-lg bg-stone-800 border border-amber-700 text-amber-300 hover:bg-amber-900/60 text-xs font-bold flex items-center space-x-1 disabled:opacity-40 disabled:cursor-not-allowed transition-all">
                        <i class="fa-solid fa-users text-amber-400"></i>
                        <span>Khán Giả</span>
                    </button>
                </div>

                <button onclick="exitQuiz()" class="text-xs text-stone-400 hover:text-amber-300">
                    <i class="fa-solid fa-right-from-bracket mr-1"></i>Thoát
                </button>
            </div>

            <!-- Hint / Audience Modal Display -->
            <div id="lifelineDisplay" class="hidden mt-3 p-3 bg-amber-950/70 border border-amber-700/60 rounded-lg text-xs text-amber-200">
                <span id="lifelineText"></span>
            </div>
        </div>
    </main>

    <!-- SCREEN 4: LEVEL RESULT MODAL -->
    <div id="resultModal" class="fixed inset-0 z-50 modal-bg hidden flex items-center justify-center p-4">
        <div class="bg-stone-900 border-2 border-amber-600 rounded-2xl w-full max-w-md p-6 text-center shadow-2xl relative ancient-border">
            <h3 id="resultTitle" class="font-title text-2xl font-bold text-amber-300 mb-1">HOÀN THÀNH MÀN CHƠI!</h3>
            <p id="resultSubtitle" class="text-xs text-amber-200/80 mb-4">Kết quả thử thách lịch sử của bạn</p>

            <!-- Star Ratings -->
            <div id="starContainer" class="flex justify-center space-x-2 mb-4 text-3xl text-stone-700">
                <i class="fa-solid fa-star transition-all duration-300"></i>
                <i class="fa-solid fa-star transition-all duration-300"></i>
                <i class="fa-solid fa-star transition-all duration-300"></i>
            </div>

            <div class="bg-stone-950/80 border border-amber-900/60 rounded-xl p-4 mb-6 space-y-2 text-sm">
                <div class="flex justify-between">
                    <span class="text-stone-400">Số câu trả lời đúng:</span>
                    <span id="resCorrect" class="text-amber-200 font-bold">0/15</span>
                </div>
                <div class="flex justify-between">
                    <span class="text-stone-400">Tổng điểm tích lũy:</span>
                    <span id="resScore" class="text-amber-400 font-bold text-lg">0</span>
                </div>
                <div class="flex justify-between text-xs pt-1 border-t border-stone-800">
                    <span class="text-stone-500">Trạng thái:</span>
                    <span id="resStatus" class="font-bold"></span>
                </div>
            </div>

            <div class="flex space-x-3">
                <button onclick="goToLevelSelect()" class="flex-1 py-3 bg-stone-800 hover:bg-stone-700 border border-amber-700 text-amber-200 font-bold rounded-xl text-sm transition-colors">
                    <i class="fa-solid fa-list mr-1"></i>Chọn Màn
                </button>
                <button id="btnNextLevel" onclick="nextLevelAction()" class="flex-1 py-3 bg-amber-600 hover:bg-amber-500 text-stone-950 font-title font-bold rounded-xl text-sm transition-colors shadow-lg">
                    Màn Tiếp <i class="fa-solid fa-arrow-right ml-1"></i>
                </button>
            </div>
        </div>
    </div>

    <!-- SETTINGS MODAL -->
    <div id="settingsModal" class="fixed inset-0 z-50 modal-bg hidden flex items-center justify-center p-4">
        <div class="bg-stone-900 border-2 border-amber-600 rounded-2xl w-full max-w-md p-6 shadow-2xl relative ancient-border">
            <div class="flex justify-between items-center pb-3 mb-4 border-b border-amber-800/60">
                <h3 class="font-title text-xl font-bold text-amber-300 flex items-center space-x-2">
                    <i class="fa-solid fa-sliders text-amber-500"></i>
                    <span>CÀI ĐẶT TRÒ CHƠI</span>
                </h3>
                <button onclick="closeSettings()" class="text-stone-400 hover:text-white w-8 h-8 rounded-full flex items-center justify-center bg-stone-800">
                    <i class="fa-solid fa-xmark text-lg"></i>
                </button>
            </div>

            <div class="space-y-4 py-2">
                <div class="flex justify-between items-center">
                    <div>
                        <div class="text-amber-200 font-semibold text-sm">Âm Thanh (SFX)</div>
                        <div class="text-xs text-stone-400">Hiệu ứng tiếng click, đúng/sai</div>
                    </div>
                    <label class="relative inline-flex items-center cursor-pointer">
                        <input type="checkbox" id="sfxToggle" checked onchange="updateSettings()" class="sr-only peer">
                        <div class="w-11 h-6 bg-stone-700 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-amber-600"></div>
                    </label>
                </div>

                <div class="flex justify-between items-center pt-2 border-t border-amber-900/30">
                    <div>
                        <div class="text-amber-200 font-semibold text-sm">Xóa Tiến Trình Chơi</div>
                        <div class="text-xs text-stone-400">Khóa các màn đã mở & reset sao</div>
                    </div>
                    <button onclick="resetProgress()" class="px-3 py-1.5 bg-rose-900/80 hover:bg-rose-800 border border-rose-600 text-rose-200 text-xs font-bold rounded-lg transition-colors">
                        Khôi Phục
                    </button>
                </div>
            </div>

            <div class="mt-6 pt-3 border-t border-amber-900/40 flex justify-end">
                <button onclick="closeSettings()" class="px-5 py-2 rounded-lg bg-amber-600 hover:bg-amber-500 text-stone-950 font-bold text-sm">
                    Hoàn Tất
                </button>
            </div>
        </div>
    </div>

    <!-- FOOTER -->
    <footer class="relative z-20 w-full p-4 text-center text-xs text-amber-600/70 border-t border-amber-950 bg-stone-950/80">
        <p>© 2026 Game Giải Đố Lịch Sử Việt Nam. Tự hào 4000 năm văn hiến dân tộc.</p>
    </footer>

    <!-- GAME LOGIC SCRIPT -->
    <script>
        // --- WEB AUDIO API SOUND SYSTEM ---
        let audioCtx = null;
        let isSoundEnabled = true;

        function initAudio() {
            if (!audioCtx) {
                audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            }
        }

        function playSound(type) {
            if (!isSoundEnabled) return;
            try {
                initAudio();
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.connect(gain);
                gain.connect(audioCtx.destination);

                if (type === 'click') {
                    osc.type = 'sine';
                    osc.frequency.setValueAtTime(400, audioCtx.currentTime);
                    osc.frequency.exponentialRampToValueAtTime(800, audioCtx.currentTime + 0.05);
                    gain.gain.setValueAtTime(0.15, audioCtx.currentTime);
                    gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.05);
                    osc.start();
                    osc.stop(audioCtx.currentTime + 0.05);
                } else if (type === 'correct') {
                    osc.type = 'triangle';
                    osc.frequency.setValueAtTime(523, audioCtx.currentTime);
                    osc.frequency.setValueAtTime(659, audioCtx.currentTime + 0.08);
                    osc.frequency.setValueAtTime(783, audioCtx.currentTime + 0.16);
                    gain.gain.setValueAtTime(0.25, audioCtx.currentTime);
                    gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.35);
                    osc.start();
                    osc.stop(audioCtx.currentTime + 0.35);
                } else if (type === 'wrong') {
                    osc.type = 'sawtooth';
                    osc.frequency.setValueAtTime(220, audioCtx.currentTime);
                    osc.frequency.setValueAtTime(160, audioCtx.currentTime + 0.12);
                    gain.gain.setValueAtTime(0.25, audioCtx.currentTime);
                    gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.25);
                    osc.start();
                    osc.stop(audioCtx.currentTime + 0.25);
                } else if (type === 'win') {
                    osc.type = 'sine';
                    osc.frequency.setValueAtTime(440, audioCtx.currentTime);
                    osc.frequency.setValueAtTime(554, audioCtx.currentTime + 0.12);
                    osc.frequency.setValueAtTime(659, audioCtx.currentTime + 0.24);
                    osc.frequency.setValueAtTime(880, audioCtx.currentTime + 0.36);
                    gain.gain.setValueAtTime(0.3, audioCtx.currentTime);
                    gain.gain.exponentialRampToValueAtTime(0.01, audioCtx.currentTime + 0.6);
                    osc.start();
                    osc.stop(audioCtx.currentTime + 0.6);
                }
            } catch (e) {
                console.log("Audio exception", e);
            }
        }

        function toggleSound() {
            isSoundEnabled = !isSoundEnabled;
            document.getElementById('soundIcon').className = isSoundEnabled ? 'fa-solid fa-volume-high text-base' : 'fa-solid fa-volume-xmark text-base text-stone-500';
            playSound('click');
        }

        // --- FULL DATABASE: 6 LEVELS x 15 QUESTIONS = 90 QUESTIONS ---
        const levelsData = [
            // LEVEL 1: Thời Cổ Đại & Chống Bắc Thuộc
            {
                id: 1,
                title: "Màn 1: Thời Kỳ Cổ Đại & Khởi Nguyên",
                difficulty: "Dễ",
                timeLimit: 25,
                icon: "fa-shield-halved",
                desc: "Thời đại Hùng Vương, Âu Lạc & các cuộc khởi nghĩa chống Bắc thuộc",
                questions: [
                    {
                        q: "Nhà nước đầu tiên trong lịch sử dân tộc Việt Nam có tên gọi là gì?",
                        options: ["Văn Lang", "Âu Lạc", "Đại Cồ Việt", "Vạn Xuân"],
                        correct: 0,
                        hint: "Do các vua Hùng đứng đầu, đóng đô ở Phong Châu (Phú Thọ).",
                        explain: "Nhà nước Văn Lang do các Vua Hùng thành lập vào khoảng thế kỷ VII TCN, đóng đô tại Phong Châu (Phú Thọ)."
                    },
                    {
                        q: "Tòa thành cổ hình xoáy trôn ốc nổi tiếng được Thục Phán An Dương Vương xây dựng tên là gì?",
                        options: ["Thành Tây Đô", "Thành Cổ Loa", "Thành Hoa Lư", "Thành Thăng Long"],
                        correct: 1,
                        hint: "Thành thuộc vùng Đông Anh, Hà Nội ngày nay.",
                        explain: "Thành Cổ Loa là kinh đô nhà nước Âu Lạc thời An Dương Vương, cấu trúc gồm 9 vòng xoáy trôn ốc độc đáo."
                    },
                    {
                        q: "Cuộc khởi nghĩa của Hai Bà Trưng chống lại ách đô hộ của nhà Hán bùng nổ vào năm nào?",
                        options: ["Năm 40", "Năm 248", "Năm 542", "Năm 938"],
                        correct: 0,
                        hint: "Hai Bà Trưng phất cờ khởi nghĩa tại Hát Môn vào đầu thế kỷ I.",
                        explain: "Năm 40 sau Công nguyên, Trưng Trắc và Trưng Nhị phất cờ khởi nghĩa tại Hát Môn, đánh đuổi Tô Định."
                    },
                    {
                        q: "Nhà nước Vạn Xuân được thành lập sau cuộc khởi nghĩa thành công của ai?",
                        options: ["Mai Thúc Loan", "Lý Nam Đế (Lý Bôn)", "Phùng Hưng", "Khúc Thừa Dụ"],
                        correct: 1,
                        hint: "Xưng hoàng đế đầu tiên của nước ta năm 544.",
                        explain: "Năm 544, sau khi đánh tan quân Lương, Lý Bôn lên ngôi lấy hiệu Lý Nam Đế và đặt tên nước là Vạn Xuân."
                    },
                    {
                        q: "Vị nữ anh hùng dân tộc nào có câu nói nổi tiếng: 'Tôi muốn cưỡi cơn gió mạnh, đạp luồng sóng dữ'?",
                        options: ["Hai Bà Trưng", "Bà Triệu (Triệu Thị Trinh)", "Bùi Thị Xuân", "Nguyên phi Ỷ Lan"],
                        correct: 1,
                        hint: "Khởi nghĩa năm 248 chống quân Đông Ngô.",
                        explain: "Bà Triệu (Triệu Thị Trinh) lãnh đạo cuộc khởi nghĩa năm 248 tại Căn cứ Phú Điền (Thanh Hóa) chống nhà Ngô."
                    },
                    {
                        q: "Ai được nhân dân tôn xưng là 'Bố Cái Đại Vương' sau khi lãnh đạo cuộc khởi nghĩa giải phóng Tống Bình?",
                        options: ["Mai Thúc Loan", "Phùng Hưng", "Khúc Thừa Dụ", "Lý Tự Tiên"],
                        correct: 1,
                        hint: "Ông quê ở Đường Lâm (Hà Nội).",
                        explain: "Phùng Hưng khởi nghĩa chống nhà Đường vào khoảng năm 776-791, sau khi mất được dân tôn vinh là Bố Cái Đại Vương."
                    },
                    {
                        q: "Khởi nghĩa Mai Thúc Loan (Mai Hắc Đế) chống lại ách đô hộ của nhà Đường bùng nổ tại đâu?",
                        options: ["Dạ Trạch (Hưng Yên)", "Hoan Châu (Nghệ An)", "Đường Lâm (Hà Nội)", "Cổ Loa (Hà Nội)"],
                        correct: 1,
                        hint: "Vùng đất miền Trung gắn liền với căn cứ Vạn An.",
                        explain: "Mai Thúc Loan xưng Mai Hắc Đế, xây dựng căn cứ Vạn An ở Hoan Châu (Nghệ An) khởi nghĩa chống nhà Đường năm 713."
                    },
                    {
                        q: "Ai là người giành lại quyền tự chủ cho dân tộc vào năm 905 khi tự xưng là Tiết độ sứ?",
                        options: ["Khúc Thừa Dụ", "Dương Đình Nghệ", "Ngô Quyền", "Kiều Công Tiễn"],
                        correct: 0,
                        hint: "Họ Khúc ở Hồng Châu (Hải Dương).",
                        explain: "Năm 905, Khúc Thừa Dụ nhân lúc nhà Đường suy yếu đã nổi dậy chiếm Tống Bình, tự xưng Tiết độ sứ."
                    },
                    {
                        q: "Nhà quân sự tài ba nào đã đánh tan quân Nam Hán trên sông Bạch Đằng năm 938?",
                        options: ["Đinh Bộ Lĩnh", "Lê Hoàn", "Ngô Quyền", "Trần Hưng Đạo"],
                        correct: 2,
                        hint: "Chủ trương dùng cọc gỗ vót nhọn cắm dưới lòng sông.",
                        explain: "Ngô Quyền dùng trận địa cọc gỗ trên sông Bạch Đằng đánh tan quân Nam Hán năm 938, mở ra kỷ nguyên độc lập."
                    },
                    {
                        q: "Vũ khí huyền thoại gắn liền với truyền thuyết An Dương Vương bảo vệ đất nước Âu Lạc là gì?",
                        options: ["Kiếm Thuận Thiên", "Nỏ Liên Châu (Nỏ Thần)", "Gậy tre Phù Đổng", "Trống đồng Đông Sơn"],
                        correct: 1,
                        hint: "Do Cao Lỗ chế tạo, có thể bắn ra hàng nghìn mũi tên.",
                        explain: "Nỏ Liên Châu (Nỏ Thần) do tướng Cao Lỗ chế tạo giúp An Dương Vương đánh bại nhiều cuộc xâm lược của Triệu Đà."
                    },
                    {
                        q: "Truyền thuyết Sơn Tinh - Thủy Tinh phản ánh hoạt động nào của người Việt cổ thời Hùng Vương?",
                        options: ["Chống giặc ngoại xâm", "Đắp đê trị thủy, phòng chống thiên tai", "Khai phá đất đai Nam Bộ", "Đổi mới thương mại"],
                        correct: 1,
                        hint: "Trận chiến giữa thần núi và thần nước.",
                        explain: "Truyền thuyết Sơn Tinh - Thủy Tinh phản ánh công cuộc đấu tranh kiên cường phòng chống lũ lụt, trị thủy của cư dân thời Văn Lang."
                    },
                    {
                        q: "Văn hóa đồ đồng rực rỡ đỉnh cao của người Việt cổ thời Hùng Vương được gọi là văn hóa gì?",
                        options: ["Văn hóa Hòa Bình", "Văn hóa Sa Huỳnh", "Văn hóa Đông Sơn", "Văn hóa Óc Eo"],
                        correct: 2,
                        hint: "Nổi tiếng với Trống Đồng.",
                        explain: "Văn hóa Đông Sơn (Thanh Hóa) đỉnh cao phát triển vào thế kỷ VII TCN - I SCN với các sản phẩm trống đồng tinh xảo."
                    },
                    {
                        q: "Tướng quân Triệu Quang Phục nối nghiệp Lý Nam Đế đã chọn căn cứ nào để đánh hiểm hóc quân Lương?",
                        options: ["Rừng Mãng Xà", "Đầm Dạ Trạch", "Hồ Lặc Thần", "Núi Ba Vì"],
                        correct: 1,
                        hint: "Được gọi là Dạ Trạch Vương.",
                        explain: "Triệu Quang Phục chọn Đầm Dạ Trạch (Hưng Yên) làm căn cứ du kích đánh du kích thành công quân Lương."
                    },
                    {
                        q: "Khởi nghĩa Hai Bà Trưng đã giải phóng được bao nhiêu thành trì ở Lĩnh Nam?",
                        options: ["36 thành", "65 thành", "100 thành", "12 thành"],
                        correct: 1,
                        hint: "Được nhắc tới trong hịch khởi nghĩa.",
                        explain: "Khởi nghĩa Hai Bà Trưng quét sạch chính quyền đô hộ, thu hồi 65 thành trì ở vùng Lĩnh Nam."
                    },
                    {
                        q: "Sự kiện nào đánh dấu mốc chấm dứt vĩnh viễn hơn 1000 năm Bắc thuộc của dân tộc ta?",
                        options: ["Khởi nghĩa Hai Bà Trưng (năm 40)", "Khởi nghĩa Lý Bôn (năm 544)", "Chiến thắng Bạch Đằng của Ngô Quyền (năm 938)", "Đinh Bộ Lĩnh lên ngôi (năm 968)"],
                        correct: 2,
                        hint: "Chiến thắng sông Bạch Đằng lừng lẫy.",
                        explain: "Trận chiến thắng Bạch Đằng năm 938 của Ngô Quyền đã chính thức kết thúc hơn 10 thế kỷ Bắc thuộc, mở ra kỷ nguyên độc lập lâu dài."
                    }
                ]
            },
            // LEVEL 2: Thời Lý - Trần - Lê (Độc Lập & Thịnh Vượng)
            {
                id: 2,
                title: "Màn 2: Độc Lập & Thịnh Vượng (Lý - Trần - Lê)",
                difficulty: "Trung Bình",
                timeLimit: 20,
                icon: "fa-dragon",
                desc: "Triều Đinh, Tiền Lê, Lý, Trần, Hậu Lê & các chiến công hiển sách",
                questions: [
                    {
                        q: "Ai là người có công dẹp loạn 12 sứ quân, thống nhất đất nước và xưng là Đinh Tiên Hoàng?",
                        options: ["Đinh Bộ Lĩnh", "Lê Hoàn", "Lý Công Uẩn", "Ngô Xương Ngập"],
                        correct: 0,
                        hint: "Gắn liền với tích dùng bông lau làm cờ trận.",
                        explain: "Đinh Bộ Lĩnh dẹp loạn 12 sứ quân, lập ra nhà nước Đại Cồ Việt năm 968, đóng đô tại Hoa Lư."
                    },
                    {
                        q: "Vua Lý Thái Tổ (Lý Công Uẩn) đã dời đô từ Hoa Lư về Đại La và đổi tên thành Thăng Long vào năm nào?",
                        options: ["Năm 938", "Năm 1010", "Năm 1258", "Năm 1428"],
                        correct: 1,
                        hint: "Năm Chiếu dời đô nổi tiếng.",
                        explain: "Mùa thu năm 1010, Vua Lý Thái Tổ ban Chiếu dời đô từ Hoa Lư về Đại La và đổi tên kinh đô thành Thăng Long."
                    },
                    {
                        q: "Bài thơ thần 'Nam quốc sơn hà' gắn liền với danh tướng nào trong trận chiến sông Như Nguyệt chống Tống?",
                        options: ["Trần Hưng Đạo", "Lý Thường Kiệt", "Lê Thạch", "Tran Quang Khải"],
                        correct: 1,
                        hint: "Tiên phát chế nhân, đánh sang đất Tống.",
                        explain: "Lý Thường Kiệt đọc bài thơ 'Nam quốc sơn hà' trên sông Như Nguyệt năm 1077 cổ vũ tinh thần quân sĩ đánh tan quân Tống."
                    },
                    {
                        q: "Nhà Trần đã từng mấy lần đánh tan quân xâm lược Nguyên Mông hung hãn?",
                        options: ["1 lần", "2 lần", "3 lần", "4 lần"],
                        correct: 2,
                        hint: "Vào các năm 1258, 1285, 1287-1288.",
                        explain: "Quân dân nhà Trần dưới sự lãnh đạo của các vua Trần và Trần Hưng Đạo đã 3 lần đánh bại quân Nguyên Mông."
                    },
                    {
                        q: "Hội nghị Diên Hồng nổi tiếng thể hiện ý chí đồng lòng quyết đánh giặc của toàn dân dưới triều đại nào?",
                        options: ["Nhà Lý", "Nhà Trần", "Nhà Lê", "Nhà Nguyễn"],
                        correct: 1,
                        hint: "Thượng hoàng Trần Thánh Tông triệu tập các bô lão.",
                        explain: "Hội nghị Diên Hồng triệu tập các bô lão cả nước tại kinh thành Thăng Long năm 1284 thời Trần để bàn kế đánh giặc."
                    },
                    {
                        q: "Bản tuyên ngôn độc lập thứ hai của dân tộc - 'Bình Ngô Đại Cáo' do ai soạn thảo?",
                        options: ["Lê Lợi", "Nguyễn Trãi", "Trần Nguyên Hãn", "Lê Văn Hưu"],
                        correct: 1,
                        hint: "Danh nhân văn hóa thế giới, cố vấn của Lê Lợi.",
                        explain: "Nguyễn Trãi thay lời Lê Lợi soạn 'Bình Ngô Đại Cáo' năm 1428 tổng kết thắng lợi của khởi nghĩa Lam Sơn chống quân Minh."
                    },
                    {
                        q: "Trận thủy chiến lừng lẫy tiêu diệt hoàn toàn ô Mã Nhi trên sông Bạch Đằng năm 1288 do ai chỉ huy?",
                        options: ["Trần Quang Khải", "Trần Khánh Dư", "Trần Quốc Tuấn (Trần Hưng Đạo)", "Trần Nhật Duật"],
                        correct: 2,
                        hint: "Tác giả Hịch tướng sĩ.",
                        explain: "Hưng Đạo Vương Trần Quốc Tuấn tái hiện trận địa cọc gỗ tiêu diệt đoàn thuyền chiến Nguyên Mông năm 1288."
                    },
                    {
                        q: "Ai là vị anh hùng dân tộc xưng vương và khởi xướng cuộc Khởi nghĩa Lam Sơn kéo dài 10 năm?",
                        options: ["Lê Lợi", "Nguyễn Trãi", "Trần Kế Xương", "Lê Lai"],
                        correct: 0,
                        hint: "Truyền thuyết trả gươm báu cho Rùa Thần ở Hồ Gươm.",
                        explain: "Lê Lợi phất cờ khởi nghĩa tại vùng núi Lam Sơn (Thanh Hóa) năm 1418, đánh tan quân Minh và lập ra nhà Hậu Lê."
                    },
                    {
                        q: "Trường đại học đầu tiên của Việt Nam được xây dựng dưới thời vua Lý Thánh Tông năm 1070 là gì?",
                        options: ["Quốc Tử Giám", "Văn Miếu", "Thái Học Viện", "Đông Kinh Nghĩa Thục"],
                        correct: 1,
                        hint: "Xây dựng năm 1070 thờ Khổng Tử, năm 1076 lập Quốc Tử Giám.",
                        explain: "Văn Miếu được xây dựng năm 1070 thời Lý Thánh Tông. Đến năm 1076, Lý Nhân Tông cho lập Quốc Tử Giám kế bên."
                    },
                    {
                        q: "Tướng quân thiếu niên nổi tiếng với lá cờ thêu 6 chữ vàng 'Phá强 địch, báo hoàng ân' thời Trần là ai?",
                        options: ["Trần Quốc Toản", "Trần Quang Khải", "Trần Bình Trọng", "Trần Khánh Dư"],
                        correct: 0,
                        hint: "Bóp nát quả cam vì chưa đủ tuổi dự họp Diên Hồng.",
                        explain: "Trần Quốc Toản vì còn nhỏ tuổi không được dự bàn việc quân đã tự bóp nát quả cam, sau đó chiêu mộ binh mã đánh giặc."
                    },
                    {
                        q: "Nhà giáo, nhà thơ kiệt xuất được tôn vinh là 'Vạn thế sư biểu' thời Trần là ai?",
                        options: ["Chu Văn An", "Trương Hán Siêu", "Mạc Đĩnh Chi", "Nguyen Bỉnh Khiêm"],
                        correct: 0,
                        hint: "Từng dâng Thất trảm sớ xin chém 7 tên nịnh thần.",
                        explain: "Chu Văn An làm Tư nghiệp Quốc Tử Giám thời Trần, nổi tiếng thanh cao và từng dâng Thất trảm sớ."
                    },
                    {
                        q: "Vị vua nào được đánh giá là đỉnh cao của nhà Hậu Lê với bộ luật Hồng Đức và hội Sáng tác Tao Đàn?",
                        options: ["Lê Thái Tổ", "Lê Thái Tông", "Lê Thánh Tông", "Lê Nhân Tông"],
                        correct: 2,
                        hint: "Triều đại Hồng Đức thịnh trị bậc nhất.",
                        explain: "Vua Lê Thánh Tông (1460 - 1497) đưa quốc gia Đại Việt phát triển rực rỡ về hành chính, pháp luật (Bộ luật Hồng Đức) và văn hóa."
                    },
                    {
                        q: "Nhà Hồ (Hồ Quý Ly) đã xây dựng tòa thành đá kiên cố độc đáo nào được UNESCO công nhận di sản thế giới?",
                        options: ["Thành Cổ Loa", "Thành Nhà Hồ (Thanh Hóa)", "Thành Huế", "Thành Sơn Tây"],
                        correct: 1,
                        hint: "Xây toàn bộ bằng các khối đá khổng lồ tại Vĩnh Lộc, Thanh Hóa.",
                        explain: "Thành Nhà Hồ được Hồ Quý Ly xây dựng năm 1397 bằng các khối đá vôi đồ xộ, là kiệt tác kiến trúc độc nhất."
                    },
                    {
                        q: "Tướng quân Trần Bình Trọng có câu nói bất tử nào trước kẻ thù Nguyên Mông?",
                        options: ["Ta thà làm ma nước Nam chứ không thèm làm vương đất Bắc", "Bao giờ người Tây nhổ hết cỏ nước Nam", "Đầu tôi chưa rơi xuống đất xin bệ hạ đừng lo", "Tôi muốn cưỡi cơn gió mạnh"],
                        correct: 0,
                        hint: "Bị địch bắt và dụ dỗ phong vương.",
                        explain: "Khi bị giặc bắt dụ dỗ hàng phong vương, Trần Bình Trọng dõng dạc trả lời: 'Ta thà làm ma nước Nam chứ không thèm làm vương đất Bắc'."
                    },
                    {
                        q: "Trận Chi Lăng - Xương Giang năm 1427 đã tiêu diệt và bắt sống tướng giặc nào của nhà Minh?",
                        options: ["Trương Phụ", "Liễu Thăng", "Mộc Thạnh", "Vương Thông"],
                        correct: 1,
                        hint: "Liễu Thăng bị chém đầu tại ải Chi Lăng.",
                        explain: "Năm 1427, nghĩa quân Lam Sơn phục kích chém chết chủ tướng Liễu Thăng tại ải Chi Lăng, buộc nhà Minh phải đầu hàng."
                    }
                ]
            },
            // LEVEL 3: Nam Bắc Phân Tranh & Tây Sơn
            {
                id: 3,
                title: "Màn 3: Nam Bắc Phân Tranh & Tây Sơn",
                difficulty: "Khó",
                timeLimit: 18,
                icon: "fa-fire",
                desc: "Trịnh - Nguyễn phân tranh, Khởi nghĩa Tây Sơn & Quang Trung đại phá quân Thanh",
                questions: [
                    {
                        q: "Giai đoạn lịch sử xung đột giữa Chúa Trịnh ở Đàng Ngoài và Chúa Nguyễn ở Đàng Trong kéo dài hàng thế kỷ lấy ranh giới ở đâu?",
                        options: ["Sông Bến Hải", "Sông Gianh (Quảng Bình)", "Sông Như Nguyệt", "Đèo Hải Vân"],
                        correct: 1,
                        hint: "Lũy Thầy do Đào Duy Từ xây dựng ở Quảng Bình.",
                        explain: "Sông Gianh và Lũy Thầy (Quảng Bình) trở thành ranh giới chia cắt Đàng Ngoài (Chúa Trịnh) và Đàng Trong (Chúa Nguyễn)."
                    },
                    {
                        q: "Ba anh em Tây Sơn khởi xướng cuộc khởi nghĩa chống chính quyền chúa Nguyễn mục nát ở Đàng Trong là ai?",
                        options: ["Nguyễn Nhạc, Nguyễn Huệ, Nguyễn Lữ", "Nguyễn Trãi, Nguyễn Huệ, Nguyễn Bỉnh Khiêm", "Nguyễn Ánh, Nguyễn Huệ, Nguyễn Lữ", "Nguyễn Hữu Cảnh, Nguyễn Nhạc, Nguyễn Huệ"],
                        correct: 0,
                        hint: "Ba anh em họ Nguyễn ở vùng Tây Sơn thượng đạo (Gia Lai/Bình Định).",
                        explain: "Ba anh em Nguyễn Nhạc, Nguyễn Huệ và Nguyễn Lữ phất cờ khởi nghĩa năm 1771 tại vùng căn cứ Tây Sơn (Bình Định)."
                    },
                    {
                        q: "Trong trận thủy chiến Rạch Gầm - Xoài Mút năm 1785, Nguyễn Huệ đã đánh tan 5 vạn quân xâm lược nào?",
                        options: ["Quân Thanh", "Quân Xiêm (Thái Lan)", "Quân Pháp", "Quân Chân Lạp"],
                        correct: 1,
                        hint: "Do Nguyễn Ánh cầu viện sang đánh Tây Sơn.",
                        explain: "Đêm 18 rạng sáng 19/1/1785, Nguyễn Huệ dùng kế phục kích đánh tan 5 vạn quân Xiêm trên sông Tiền (Rạch Gầm - Xoài Mút)."
                    },
                    {
                        q: "Nguyễn Huệ làm lễ lên ngôi Hoàng đế lấy niên hiệu là Quang Trung tại đâu trước khi ra Bắc đánh quân Thanh?",
                        options: ["Quy Nhơn", "Thăng Long", "Núi Bàn Sơn (Phú Xuân - Huế)", "Hoa Lư"],
                        correct: 2,
                        hint: "Núi Bàn Sơn (Phú Xuân - Huế) tháng 12 năm 1788.",
                        explain: "Ngày 22/12/1788 (25 tháng Chạp), Nguyễn Huệ đắp đài ở núi Bàn Sơn (Huế) lên ngôi Hoàng đế, lấy hiệu Quang Trung."
                    },
                    {
                        q: "Trận chiến lừng lẫy tiêu diệt 29 vạn quân Thanh mùa xuân năm Kỷ Dậu (1789) gắn liền với căn cứ tiến công nổi tiếng nào?",
                        options: ["Ngọc Hồi - Đống Đa", "Rạch Gầm - Xoài Mút", "Chi Lăng - Xương Giang", "Tốt Động - Chúc Động"],
                        correct: 0,
                        hint: "Vào đêm Mùng 4 rạng sáng Mùng 5 Tết Kỷ Dậu.",
                        explain: "Mùng 5 Tết Kỷ Dậu 1789, quân Tây Sơn hạ đồn Ngọc Hồi và Đống Đa, giải phóng Thăng Long, tướng Sầm Nghi Đống thắt cổ tự tử."
                    },
                    {
                        q: "Nữ danh tướng Tây Sơn nổi tiếng với tài phi phượng kiếm và chỉ huy đội tượng binh mãnh liệt là ai?",
                        options: ["Triệu Thị Trinh", "Bùi Thị Xuân", "Nguyễn Thị Định", "Lê Thị Hồng Phong"],
                        correct: 1,
                        hint: "Vợ của đô đốc Trần Quang Diệu.",
                        explain: "Bùi Thị Xuân là nữ danh tướng kiệt xuất của triều Tây Sơn, người chỉ huy đội voi chiến làm quân thù khiếp sợ."
                    },
                    {
                        q: "Ai là người có công khai phá và thành lập Dinh Thống Nhất/Phủ Gia Định (Sài Gòn ngày nay) vào năm 1698?",
                        options: ["Nguyễn Hữu Cảnh", "Nguyễn Hoàng", "Đào Duy Từ", "Mạc Cửu"],
                        correct: 0,
                        hint: "Lễ thành hầu Nguyễn Hữu Cảnh.",
                        explain: "Năm 1698, Lễ Thành Hầu Nguyễn Hữu Cảnh được chúa Nguyễn Phúc Chu cử vào kinh lý phía Nam, lập ra Phủ Gia Định."
                    },
                    {
                        q: "Tác giả của tác phẩm nổi tiếng 'Truyện Kiều' - danh nhân văn hóa thế giới sống vào cuối thời Tây Sơn đầu nhà Nguyễn là ai?",
                        options: ["Nguyễn Trãi", "Nguyễn Du", "Hồ Xuân Hương", "Đoàn Thị Điểm"],
                        correct: 1,
                        hint: "Tên chữ là Tố Như, hiệu Thanh Hiên.",
                        explain: "Đại thi hào Nguyễn Du (1765 - 1820) tác giả tác phẩm Đoạn Trường Tân Thanh (Truyện Kiều) đạt đỉnh cao thi văn dân tộc."
                    },
                    {
                        q: "Danh sĩ nổi tiếng thời Trịnh - Nguyễn phân tranh được mệnh danh là Trạng Trình với những lời sấm truyền chính xác là ai?",
                        options: ["Chu Văn An", "Nguyễn Bỉnh Khiêm", "Lê Quý Đôn", "Phùng khắc Khoan"],
                        correct: 1,
                        hint: "Câu nói 'Hoành Sơn nhất dải vạn đại dung thân'.",
                        explain: "Nguyễn Bỉnh Khiêm (Trạng Trình) là nhà triết học, nhà dự báo thiên tài thời Mạc - Trịnh - Nguyễn."
                    },
                    {
                        q: "Tướng giặc nào của nhà Thanh phải thắt cổ tự tử tại gò Đống Đa khi bị quân Tây Sơn công phá?",
                        options: ["Tôn Sĩ Nghị", "Sầm Nghi Đống", "Hứa Thế Hanh", "Thượng維 Thanh"],
                        correct: 1,
                        hint: "Chỉ huy đồn Đống Đa.",
                        explain: "Sầm Nghi Đống - Thái thú Điền Châu chỉ huy đồn Đống Đa tuyệt vọng thắt cổ tự tử trên cây đa ở gò Đống Đa sáng mùng 5 Tết."
                    },
                    {
                        q: "Nhiều cải cách tiến bộ về chữ Nôm, ruộng đất và giáo dục được thực hiện dưới triều đại vua nào?",
                        options: ["Vua Quang Trung", "Vua Gia Long", "Vua Minh Mạng", "Vua Lê Hiển Tông"],
                        correct: 0,
                        hint: "Vua ban chiếu dịch sách kinh điển sang chữ Nôm.",
                        explain: "Vua Quang Trung đề cao chữ Nôm làm quốc ngữ, lập Sùng Dĩnh Viện và ban Chiếu khuyến học, Chiếu tịch điền."
                    },
                    {
                        q: "Ai là vị chúa Nguyễn đầu tiên vượt Hoành Sơn vào khai phá xứ Thuận Hóa năm 1558?",
                        options: ["Chúa Nguyễn Hoàng (Chúa Tiên)", "Chúa Nguyễn Phúc Nguyên", "Chúa Nguyễn Phúc Chu", "Chúa Nguyễn Ánh"],
                        correct: 0,
                        hint: "Người nghe lời khuyên của Trạng Trình Nguyễn Bỉnh Khiêm.",
                        explain: "Năm 1558, Nguyễn Hoàng xin vào trấn thủ Thuận Hóa, mở đầu cho công cuộc mở cõi về phía Nam của các Chúa Nguyễn."
                    },
                    {
                        q: "Quân Tây Sơn sử dụng phương tiện tác chiến đặc biệt nào làm nòng cốt trong đại phá quân Thanh ở Ngọc Hồi?",
                        options: ["Tàu chiến bọc đồng", "Tượng binh (Đội voi chiến) kết hợp rồng lửa", "Xe bọc thép gỗ", "Kinh khí cầu"],
                        correct: 1,
                        hint: "Đội voi chiến mang đại bác và rồng lửa.",
                        explain: "Vua Quang Trung sử dụng lực lượng Tượng binh mang hỏa pháo cùng ván rơm bọc ướt xông thẳng phá đồn lũy quân Thanh."
                    },
                    {
                        q: "Nhà bác học, nhà thư tịch lớn nhất Việt Nam thế kỷ XVIII tác giả bộ 'Vân Đài Loại Ngữ' là ai?",
                        options: ["Nguyễn Trãi", "Lê Quý Đôn", "Phan Huy Chú", "Ngo Thì Nhậm"],
                        correct: 1,
                        hint: "Được mệnh danh là túi khôn của thời đại.",
                        explain: "Lê Quý Đôn (1726 - 1784) là nhà bác học vĩ đại thời Lê - Trịnh, tác giả của hàng chục bộ sách lịch sử, địa lý, triết học."
                    },
                    {
                        q: "Chúa Nguyễn Phúc Chu đã cho lực lượng hải quân xác lập chủ quyền liên tục tại quần đảo Hoàng Sa và Trường Sa qua đội nào?",
                        options: ["Đội Hải quân Gia Định", "Đội Hoàng Sa & Đội Bắc Hải", "Vệ binh Duyên hải", "Đội Thủy thủ Nam Hải"],
                        correct: 1,
                        hint: "Thu gom đồi hon, sản vật và đo đạc hải trình.",
                        explain: "Các Chúa Nguyễn đã thành lập Đội Hoàng Sa và Đội Bắc Hải ra quần đảo Hoàng Sa, Trường Sa khai thác sản vật và khẳng định chủ quyền."
                    }
                ]
            },
            // LEVEL 4: Thời Nhà Nguyễn & Phong Trào Chống Pháp
            {
                id: 4,
                title: "Màn 4: Nhà Nguyễn & Chống Thực Dân Pháp",
                difficulty: "Khó",
                timeLimit: 15,
                icon: "fa-landmark",
                desc: "Nhà Nguyễn lập quốc, Pháp xâm lược & phong trào Cần Vương, Duy Tân",
                questions: [
                    {
                        q: "Ai là người đánh bại triều Tây Sơn, thành lập Nhà Nguyễn vào năm 1802 và lấy niên hiệu Gia Long?",
                        options: ["Nguyễn Ánh", "Nguyễn Phúc Đảm", "Nguyễn Phúc Vĩnh Thụy", "Nguyễn Huệ"],
                        correct: 0,
                        hint: "Vua đầu tiên của nhà Nguyễn.",
                        explain: "Năm 1802, Nguyễn Ánh lên ngôi Hoàng đế lấy hiệu Gia Long, đặt tên nước là Việt Nam và chọn Phú Xuân (Huế) làm kinh đô."
                    },
                    {
                        q: "Thực dân Pháp chính thức nổ súng nã đại bác xâm lược Việt Nam tại đâu vào ngày 01/09/1858?",
                        options: ["Thành Hà Nội", "Cảng Đà Nẵng", "Gia Định", "Huế"],
                        correct: 1,
                        hint: "Bán đảo Sơn Trà - Đà Nẵng.",
                        explain: "Chiều 31/8/1858 và rạng sáng 1/9/1858, liên quân Pháp - Tây Ban Nha nổ súng tấn công bán đảo Sơn Trà (Đà Nẵng)."
                    },
                    {
                        q: "Vị anh hùng Nam Kỳ nào nổi tiếng với trận đốt tàu Hy Vọng (Espérance) của Pháp trên sông Nhật Tảo năm 1861?",
                        options: ["Trương Định", "Nguyễn Trung Trực", "Thiên Hộ Dương", "Phan Tôn"],
                        correct: 1,
                        hint: "Câu nói: 'Bao giờ người Tây nhổ hết cỏ nước Nam...'",
                        explain: "Nguyễn Trung Trực lãnh đạo nghĩa quân đốt cháy tàu chiến Espérance của Pháp trên sông Nhật Tảo ngày 10/12/1861."
                    },
                    {
                        q: "Sau khi kinh thành Huế thất thủ, Vua Hàm Nghi đã ban chiếu gì phát động phong trào chống Pháp trong cả nước?",
                        options: ["Chiếu dời đô", "Chiếu Cần Vương", "Chiếu khuyến học", "Hịch tướng sĩ"],
                        correct: 1,
                        hint: "Ban hành tháng 7 năm 1885 tại Tân Sở (Quảng Trị).",
                        explain: "Đêm 13/7/1885, Tôn Thất Thuyết đưa Vua Hàm Nghi ra Tân Sở (Quảng Trị) ban Chiếu Cần Vương kêu gọi sĩ phu và nhân dân giúp vua cứu nước."
                    },
                    {
                        q: "Khởi nghĩa Hương Khê - cuộc khởi nghĩa lớn nhất trong phong trào Cần Vương do ai lãnh đạo?",
                        options: ["Ba Đình", "Phan Đình Phùng & Cao Thắng", "Hoàng Hoa Thám", "Nguyen Quang Bích"],
                        correct: 1,
                        hint: "Căn cứ ở Ngàn Trụ (Hà Tĩnh), Cao Thắng chế tạo súng kiểu Pháp.",
                        explain: "Phan Đình Phùng cùng tướng quân Cao Thắng lãnh đạo khởi nghĩa Hương Khê (1885 - 1896) chế tạo súng trường kiên cường chống Pháp."
                    },
                    {
                        q: "Ai được mệnh danh là 'Hùm xám Yên Thế', lãnh đạo cuộc khởi nghĩa nông dân Yên Thế kéo dài gần 30 năm?",
                        options: ["Hoàng Hoa Thám (Đề Thám)", "Phan Đình Phùng", "Nguyen Thiện Thuật", "Cầm Đắc Quản"],
                        correct: 0,
                        hint: "Căn cứ vùng núi Yên Thế (Bắc Giang).",
                        explain: "Hoàng Hoa Thám (Đề Thám) lãnh đạo cuộc khởi nghĩa Yên Thế (1884 - 1913) gây cho quân Pháp nhiều tổn thất nặng nề."
                    },
                    {
                        q: "Nhà yêu nước Phan Bội Châu đã khởi xướng phong trào nào đưa thanh niên Việt Nam sang Nhật Bản học tập?",
                        options: ["Phong trào Duy Tân", "Phong trào Đông Du", "Đông Kinh Nghĩa Thục", "Hội Việt Nam Cách mạng Thanh niên"],
                        correct: 1,
                        hint: "Đưa học sinh đi về phía Đông (Nhật Bản).",
                        explain: "Năm 1905, Phan Bội Châu thành lập Duy Tân hội và khởi xướng Phong trào Đông Du đưa thanh niên sang Nhật học tập cứu quốc."
                    },
                    {
                        q: "Nhà cách mạng Phan Châu Trinh nổi tiếng với chủ trương cứu nước bằng phương pháp nào?",
                        options: ["Bạo động vũ trang", "Cải cách nâng cao dân trí, dân quyền ('Khai dân trí,振 dân khí')", "Thỉnh nguyện lên Vua", "Trưng cầu ý dân"],
                        correct: 1,
                        hint: "Khai dân trí,振 dân khí, hậu dân sinh.",
                        explain: "Phan Châu Trinh đề xướng phong trào Duy Tân theo xu hướng cải cách: 'Khai dân trí,振 dân khí, hậu dân sinh'."
                    },
                    {
                        q: "Tổng đốc thành Hà Nội nào đã tuẫn tiết khi thành Hà Nội bị quân Pháp thất thủ lần thứ hai năm 1882?",
                        options: ["Nguyễn Tri Phương", "Hoàng Diệu", "Phan Thanh Giản", "Trương Đăng Cửu"],
                        correct: 1,
                        hint: "Treo cổ tuẫn tiết tại Võ Miếu.",
                        explain: "Ngày 25/4/1882, khi quân Pháp chiếm thành Hà Nội, Tổng đốc Hoàng Diệu đã thắt cổ tuẫn tiết tại Võ Miếu để giữ trọn khí tiết."
                    },
                    {
                        q: "Cùng với Hoàng Diệu, vị Tổng đốc nào đã nhịn ăn tuẫn tiết khi thành Hà Nội thất thủ lần thứ nhất năm 1873?",
                        options: ["Nguyễn Tri Phương", "Phan Thanh Giản", "Truơng Định", "Nguyen Văn Tường"],
                        correct: 0,
                        hint: "Danh tướng chỉ huy trận tuyến Đà Nẵng và Gia Định.",
                        explain: "Nguyễn Tri Phương bị thương nặng khi giữ thành Hà Nội năm 1873, ông khước từ sự cứu chữa của Pháp và từ chối ăn uống cho đến chết."
                    },
                    {
                        q: "Bản đồ toàn thư và bộ đại địa chí lớn nhất nhà Nguyễn mang tên 'Đại Nam Nhất Thống Chí' hoàn thành dưới triều vua nào?",
                        options: ["Vua Gia Long", "Vua Minh Mạng", "Vua Tự Đức", "Vua Đồng Khánh"],
                        correct: 2,
                        hint: "Biên soạn bởi Quốc Sử Quán nhà Nguyễn.",
                        explain: "Đại Nam Nhất Thống Chí là bộ chí lược địa lý đồ sộ nhất do Quốc Sử Quán triều Nguyễn biên soạn thời Tự Đức."
                    },
                    {
                        q: "Trường Đông Kinh Nghĩa Thục (1907) do Lương Văn Can và Nguyễn Quyền thành lập tại Hà Nội hoạt động chính theo mô hình nào?",
                        options: ["Trường huấn luyện quân sự", "Trường học tân tiến dạy chữ Quốc ngữ miễn phí", "Xưởng chế tạo vũ khí", "Hội thương gia buôn bán"],
                        correct: 1,
                        hint: "Dạy chữ Quốc ngữ, diễn thuyết truyền bá tư tưởng mới.",
                        explain: "Đông Kinh Nghĩa Thục thành lập tháng 3/1907 tại Hà Nội, dạy học miễn phí chữ Quốc ngữ và truyền bá tri thức tiến bộ."
                    },
                    {
                        q: "Trận đồn Ba Đình (Thanh Hóa) nổi tiếng trong phong trào Cần Vương do những ai lãnh đạo?",
                        options: ["Phạm Bành & Đinh Công Tráng", "Phan Đình Phùng", "Nguyen Thiện Thuật", "Phan Bội Châu"],
                        correct: 0,
                        hint: "Căn cứ Ba Đình cấu trúc gồm 3 làng Mỹ Khê, Thượng Thọ, Mậu Thị.",
                        explain: "Cuộc khởi nghĩa Ba Đình (1886 - 1887) do Phạm Bành và Đinh Công Tráng chỉ huy xây dựng chiến lũy chống Pháp kiên cường."
                    },
                    {
                        q: "Vua Minh Mạng đã thực hiện cuộc cải cách hành chính lớn năm 1831 - 1832 chia cả nước thành bao nhiêu tỉnh?",
                        options: ["24 tỉnh", "30 tỉnh và 1 phủ Thừa Thiên", "64 tỉnh", "12 tỉnh"],
                        correct: 1,
                        hint: "Đặt ra chức Tổng đốc và Tuần phủ.",
                        explain: "Vua Minh Mạng bãi bỏ Bắc Thành và Gia Định Thành, chia cả nước thành 30 tỉnh và 1 phủ Thừa Thiên."
                    },
                    {
                        q: "Vị vua trẻ yêu nước nào của Triều Nguyễn đã bị Pháp lưu đày sang đảo Réunion cùng Vua Thành Thái và Duy Tân?",
                        options: ["Vua Hàm Nghi", "Vua Khải Định", "Vua Đồng Khánh", "Vua Bảo Đại"],
                        correct: 0,
                        hint: "Lên núi ban Chiếu Cần Vương khi mới 14 tuổi.",
                        explain: "Vua Hàm Nghi bị giặc Pháp bắt năm 1888 và đày sang Algérie; trong khi Vua Thành Thái và Duy Tân bị đày sang đảo Réunion."
                    }
                ]
            },
            // LEVEL 5: Cách Mạng & Kháng Chiến Chống Pháp (1930 - 1954)
            {
                id: 5,
                title: "Màn 5: Cách Mạng & Kháng Chiến Chống Pháp",
                difficulty: "Rất Khó",
                timeLimit: 12,
                icon: "fa-star",
                desc: "Đảng thành lập 1930, Cách mạng Tháng 8 năm 1945 & Chiến thắng Điện Biên Phủ 1954",
                questions: [
                    {
                        q: "Người thanh niên Nguyễn Tất Thành (Chủ tịch Hồ Chí Minh) ra đi tìm đường cứu nước tại Cảng Nhà Rồng vào ngày tháng năm nào?",
                        options: ["05/06/1911", "19/05/1890", "03/02/1930", "02/09/1945"],
                        correct: 0,
                        hint: "Rời quê hương trên chiếc tàu Amiral Latouche-Tréville.",
                        explain: "Ngày 5/6/1911, người thanh niên Nguyễn Tất Thành rời cảng Nhà Rồng (Sài Gòn) sang phương Tây tìm đường giải phóng dân tộc."
                    },
                    {
                        q: "Đảng Cộng sản Việt Nam được thành lập vào ngày 03/02/1930 tại đâu do Nguyễn Ai Quốc chủ trì?",
                        options: ["Hà Nội", "Hương Cảng (Hồng Kông, Trung Quốc)", "Quảng Châu", "Cao Bằng"],
                        correct: 1,
                        hint: "Hội nghị hợp nhất các tổ chức cộng sản tại Cửu Long (Hồng Kông).",
                        explain: "Từ ngày 6/1 đến 7/2/1930, Hội nghị hợp nhất Đảng do Nguyễn Ái Quốc chủ trì diễn ra tại Bán Đảo Cửu Long (Hồng Kông)."
                    },
                    {
                        q: "Bản Tuyên ngôn Độc lập khai sinh ra nước Việt Nam Dân chủ Cộng hòa được Bác Hồ đọc tại Quảng trường Ba Đình vào ngày nào?",
                        options: ["19/08/1945", "02/09/1945", "19/12/1946", "07/05/1954"],
                        correct: 1,
                        hint: "Ngày Quốc khánh Việt Nam.",
                        explain: "Ngày 2/9/1945, tại Quảng trường Ba Đình (Hà Nội), Chủ tịch Hồ Chí Minh đọc bản Tuyên ngôn Độc lập khai sinh nước VNDCCH."
                    },
                    {
                        q: "Lời kêu gọi 'Toàn quốc kháng chiến' chống thực dân Pháp được Chủ tịch Hồ Chí Minh ban hành vào thời điểm nào?",
                        options: ["Đêm 19/12/1946", "02/09/1945", "19/08/1945", "10/10/1954"],
                        correct: 0,
                        hint: "Mở đầu 60 ngày đêm chiến đấu bảo vệ Thủ đô.",
                        explain: "Đêm 19/12/1946, Chủ tịch Hồ Chí Minh ra Lời kêu gọi Toàn quốc kháng chiến: 'Chúng ta thà hi sinh tất cả chứ nhất định không chịu mất nước...'"
                    },
                    {
                        q: "Chiến dịch lịch sử nào năm 1954 'lừng lẫy năm châu, chấn động địa cầu' buộc Pháp phải ký Hiệp định Giơ-ne-vơ?",
                        options: ["Chiến dịch Việt Bắc (1947)", "Chiến dịch Biên giới (1950)", "Chiến dịch Điện Biên Phủ (1954)", "Chiến dịch Tây Bắc (1952)"],
                        correct: 2,
                        hint: "Sau 56 ngày đêm khoét núi, ngủ hầm, mưa dầm, cơm nắm.",
                        explain: "Chiến dịch Điện Biên Phủ kéo dài 56 ngày đêm (13/3 - 7/5/1954) tiêu diệt tập đoàn căn cứ điểm của Pháp, kết thúc kháng chiến chống Pháp."
                    },
                    {
                        q: "Tướng chỉ huy quân Pháp tại tập đoàn căn cứ điểm Điện Biên Phủ bị quân ta bắt sống vào chiều 07/05/1954 là ai?",
                        options: ["Tướng De Castries (Đề Cát-tơ-ri)", "Tướng Navarre", "Tướng Salan", "Tướng Cogny"],
                        correct: 0,
                        hint: "Bị bắt sống tại hầm chỉ huy trung tâm.",
                        explain: "Chiều 7/5/1954, lá cờ 'Quyết chiến Quyết thắng' tung bay trên nóc hầm De Castries, tướng De Castries cùng toàn bộ bộ tham mưu bị bắt."
                    },
                    {
                        q: "Tổng chỉ huy kiệt xuất của Quân đội Nhân dân Việt Nam trong chiến dịch Điện Biên Phủ là ai?",
                        options: ["Đại tướng Văn Tiến Dũng", "Đại tướng Võ Nguyên Giáp", "Đại tướng Nguyễn Chí Thanh", "Đại tướng Hoàng Văn Thái"],
                        correct: 1,
                        hint: "Người anh cả của Quân đội Nhân dân Việt Nam.",
                        explain: "Đại tướng Võ Nguyên Giáp là Tổng chỉ huy trực tiếp chỉ đạo Chiến dịch Điện Biên Phủ với quyết định lịch sử chuyển 'Đánh nhanh thắng nhanh' sang 'Đánh chắc tiến chắc'."
                    },
                    {
                        q: "Anh hùng liệt sĩ nào đã lấy thân mình lấp lỗ châu mai trong chiến dịch Điện Biên Phủ?",
                        options: ["Bế Văn Đàn", "Tô Vĩnh Diện", "Phan Đình Giót", "Núp"],
                        correct: 2,
                        hint: "Trận hỏa lực tại Him Lam ngày 13/03/1954.",
                        explain: "Phan Đình Giót đã dũng cảm lao lên lấy thân mình lấp lỗ châu mai hỏa lực địch tại trận Him Lam mở đường cho đồng đội xông lên."
                    },
                    {
                        q: "Anh hùng liệt sĩ nào đã lấy thân mình chèn bánh pháo không cho pháo lăn xuống vực tại chiến dịch Điện Biên Phủ?",
                        options: ["Tô Vĩnh Diện", "Bế Văn Đàn", "Cù Chính Lan", "Nguyen Thị Chiên"],
                        correct: 0,
                        hint: "Cứu khẩu pháo cao xạ 37mm.",
                        explain: "Anh hùng Tô Vĩnh Diện đã dũng cảm lấy thân mình chèn bánh khẩu pháo cao xạ 37mm khi dây tời bị đứt trên dốc kéo pháo."
                    },
                    {
                        q: "Đội Việt Nam Tuyên truyền Giải phóng quân (tiền thân của QĐND Việt Nam) được thành lập vào ngày tháng năm nào?",
                        options: ["22/12/1944", "19/08/1945", "15/05/1945", "03/02/1930"],
                        correct: 0,
                        hint: "Ngày thành lập Quân đội Nhân dân Việt Nam.",
                        explain: "Ngày 22/12/1944, Đội VN Tuyên truyền Giải phóng quân gồm 34 chiến sĩ thành lập tại khu rừng Trần Hưng Đạo (Cao Bằng) do Võ Nguyên Giáp chỉ huy."
                    },
                    {
                        q: "Chiến dịch Biên giới Thu - Đông 1950 là chiến dịch đầu tiên Bác Hồ trực tiếp ra mặt trận quan sát chỉ đạo tại căn cứ nào?",
                        options: ["Đông Khê", "Thất Khê", "Mường Thanh", "Tân Trào"],
                        correct: 0,
                        hint: "Hình ảnh Bác Hồ chống gậy trên đỉnh núi quan sát trận địa.",
                        explain: "Tại Chiến dịch Biên giới 1950, Bác Hồ trực tiếp lên quan sát trận đánh đồn Đông Khê (Cao Bằng)."
                    },
                    {
                        q: "Khởi nghĩa Xô Viết Nghệ Tĩnh (1930 - 1931) đỉnh cao bùng nổ mạnh mẽ nhất vào ngày kỷ niệm nào?",
                        options: ["Ngày Quốc tế Lao động 01/05/1930", "Ngày 19/08", "Ngày 02/09", "Ngày 03/02"],
                        correct: 0,
                        hint: "Ngày hội lao động toàn thế giới.",
                        explain: "Phong trào Xô viết Nghệ Tĩnh bùng nổ từ ngày 1/5/1930 với các cuộc biểu tình rầm rộ của công nông Nghệ An và Hà Tĩnh."
                    },
                    {
                        q: "Mặt trận Việt Minh (Việt Nam Độc lập Đồng minh) được Nguyễn Ái Quốc thành lập vào năm nào tại Pắc Bó (Cao Bằng)?",
                        options: ["1930", "1941", "1945", "1950"],
                        correct: 1,
                        hint: "Tháng 5 năm 1941 tại Hội nghị Trung ương Đảng lần 8.",
                        explain: "Ngày 19/5/1941, Mặt trận Việt Minh thành lập tại Pắc Bó (Cao Bằng) nhằm đoàn kết toàn dân chống Pháp - Nhật."
                    },
                    {
                        q: "Tổ chức cách mạng tiền thân của Đảng Cộng sản do Nguyễn Ái Quốc thành lập năm 1925 tại Quảng Châu có tên là gì?",
                        options: ["Hội Việt Nam Cách mạng Thanh niên", "Tân Việt Cách mạng Đảng", "Việt Nam Quốc dân Đảng", "Hội Liên hiệp Quốc tế"],
                        correct: 0,
                        hint: "Xuất bản báo Thanh niên.",
                        explain: "Tháng 6/1925, Nguyễn Ái Quốc thành lập Hội Việt Nam Cách mạng Thanh niên tại Quảng Châu (Trung Quốc) để đào tạo cán bộ."
                    },
                    {
                        q: "Hiệp định Giơ-ne-vơ ký kết ngày 21/07/1954 đã lấy vĩ tuyến nào làm ranh giới quân sự tạm thời ở Việt Nam?",
                        options: ["Vĩ tuyến 13", "Vĩ tuyến 17 (Sông Bến Hải - Quảng Trị)", "Vĩ tuyến 16", "Vĩ tuyến 20"],
                        correct: 1,
                        hint: "Cầu Hiền Lương - Sông Bến Hải.",
                        explain: "Hiệp định Giơ-ne-vơ 1954 quy định lấy vĩ tuyến 17 (sông Bến Hải, Quảng Trị) làm giới tuyến quân sự tạm thời trước khi tổng tuyển cử."
                    }
                ]
            },
            // LEVEL 6: Kháng Chiến Chống Mỹ & Thống Nhất Nước Nhà (1954 - Nay)
            {
                id: 6,
                title: "Màn 6: Kháng Chiến Chống Mỹ & Thống Nhất",
                difficulty: "Siêu Khó",
                timeLimit: 10,
                icon: "fa-flag",
                desc: "Phong trào Đồng Khởi, Mậu Thân 1968, Điện Biên Phủ trên không & Đại thắng 30/4/1975",
                questions: [
                    {
                        q: "Phong trào 'Đồng Khởi' nổi dậy tiêu biểu nhất bùng nổ đầu năm 1960 gắn liền với tên tuổi nữ tướng Nguyễn Thị Định tại tỉnh nào?",
                        options: ["Bến Tre", "Mỹ Tho", "Tây Ninh", "Cà Mau"],
                        correct: 0,
                        hint: "Đội quân tóc dài huyền thoại.",
                        explain: "Phong trào Đồng Khởi bùng nổ từ tháng 1/1960 tại huyện Định Thủy, Phước Hiệp, Bình Khánh (Bến Tre) lan rộng khắp miền Nam."
                    },
                    {
                        q: "Tuyến đường chiến lược nối liền hậu phương Miền Bắc tiếp tế cho tiền tuyến Miền Nam mang tên vị lãnh tụ nào?",
                        options: ["Đường Quốc lộ 1A", "Đường Trường Sơn (Đường Hồ Chí Minh)", "Đường Đường Bách Việt", "Đường Hùng Vương"],
                        correct: 1,
                        hint: "Khai thông ngày 19/05/1959.",
                        explain: "Đoàn 559 thành lập ngày 19/5/1959 mở tuyến đường Trường Sơn (Đường Hồ Chí Minh) huyền thoại chi viện cho miền Nam."
                    },
                    {
                        q: "Cuộc Tổng tiến công và nổi dậy Mậu Thân đồng loạt đánh vào các đô thị miền Nam diễn ra vào năm nào?",
                        options: ["1965", "1968", "1972", "1975"],
                        correct: 1,
                        hint: "Đêm giao thừa Tết Mậu Thân.",
                        explain: "Đêm Mùng 1 rạng sáng Mùng 2 Tết Mậu Thân (1968), quân dân ta đồng loạt tiến công 64 đô thị miền Nam, làm phá sản chiến lược 'Chiến tranh cục bộ'."
                    },
                    {
                        q: "Trận chiến 12 ngày đêm đánh bại máy bay B-52 của Mỹ bảo vệ Hà Nội cuối năm 1972 được gọi là gì?",
                        options: ["Chiến dịch Đường 9 - Nam Lào", "Chiến thắng Điện Biên Phủ trên không", "Trận Trại David", "Chiến dịch Khe Sanh"],
                        correct: 1,
                        hint: "Từ 18/12 đến 30/12/1972.",
                        explain: "Trận 'Điện Biên Phủ trên không' diễn ra 12 ngày đêm từ 18 - 30/12/1972 bắn rơi 81 máy bay Mỹ (trong đó có 34 máy bay B-52)."
                    },
                    {
                        q: "Hiệp định ngoại giao lịch sử buộc Mỹ phải rút toàn bộ quân đội về nước được ký kết tại đâu vào ngày 27/01/1973?",
                        options: ["Hiệp định Giơ-ne-vơ", "Hiệp định Pa-ri (Paris)", "Hiệp định Lơ Bông", "Hiệp định Mã Lai"],
                        correct: 1,
                        hint: "Thủ đô nước Pháp.",
                        explain: "Hiệp định Paris được ký kết ngày 27/1/1973 tại Paris (Pháp), chấm dứt chiến tranh, lập lại hòa bình ở Việt Nam."
                    },
                    {
                        q: "Bộ chính trị đã quyết định đổi tên 'Chiến dịch Giải phóng Sài Gòn - Gia Định' thành tên chiến dịch nào?",
                        options: ["Chiến dịch Tây Nguyên", "Chiến dịch Huế - Đà Nẵng", "Chiến dịch Hồ Chí Minh", "Chiến dịch Quang Trung"],
                        correct: 2,
                        hint: "Quyết định ngày 14/04/1975.",
                        explain: "Ngày 14/4/1975, Bộ Chính trị quyết định đổi tên Chiến dịch giải phóng Sài Gòn - Gia Định thành Chiến dịch Hồ Chí Minh."
                    },
                    {
                        q: "Chiếc xe tăng mang số hiệu nào của quân giải phóng đã húc văng cổng chính Dinh Độc Lập vào trưa ngày 30/04/1975?",
                        options: ["Xe tăng 390", "Xe tăng 843", "Xe tăng 559", "Xe tăng 117"],
                        correct: 0,
                        hint: "Xe tăng húc đổ cánh cổng chính (xe 843 húc cổng phụ).",
                        explain: "Lúc 10h45 ngày 30/4/1975, xe tăng 390 húc văng cổng chính Dinh Độc Lập, theo sau xe tăng 843 tiến vào."
                    },
                    {
                        q: "Chiến sĩ đại đội trưởng nào đã cắm lá cờ chiến thắng của Mặt trận Dân tộc Giải phóng lên nóc Dinh Độc Lập trưa 30/04/1975?",
                        options: ["Bùi Quang Thận", "Vũ Đăng Toàn", "Nguyen Văn Kỷ", "Ngo Sỹ Nguyên"],
                        correct: 0,
                        hint: "Chỉ huy xe tăng 843.",
                        explain: "Trung úy Bùi Quang Thận (Đại đội trưởng Đại đội 4 xe tăng) đã chạy lên cắm cờ trên nóc Dinh Độc Lập lúc 11h30 ngày 30/4/1975."
                    },
                    {
                        q: "Tổng thống cuối cùng của chính quyền Sài Gòn phải tuyên bố tuyên bố bố đầu hàng không điều kiện ngày 30/4/1975 là ai?",
                        options: ["Nguyễn Văn Thiệu", "Trần Văn Hương", "Dương Văn Minh", "Nguyễn Cao Kỳ"],
                        correct: 2,
                        hint: "Đại tướng Dương Văn Minh.",
                        explain: "Tổng thống Dương Văn Minh đọc lời tuyên bố đầu hàng không điều kiện trên đài phát thanh Sài Gòn trưa ngày 30/4/1975."
                    },
                    {
                        q: "Quốc hội khóa VI năm 1976 đã quyết định đổi tên thành phố Sài Gòn - Gia Định thành tên gọi nào?",
                        options: ["Thành phố Hồ Chí Minh", "Thành phố Nam Bộ", "Thành phố Cửu Long", "Thành phố Gia Định"],
                        correct: 0,
                        hint: "Mang tên Bác Hồ kính yêu.",
                        explain: "Ngày 2/7/1976, Quốc hội nước Việt Nam thống nhất quyết định chính thức đổi tên thành phố Sài Gòn - Gia Định thành Thành phố Hồ Chí Minh."
                    },
                    {
                        q: "Đại hội Đảng toàn quốc lần thứ VI năm 1986 đã đề ra đường lối chiến lược lịch sử nào cho đất nước?",
                        options: ["Đường lối Đổi Mới toàn diện", "Đường lối công nghiệp hóa thần tốc", "Đường lối tập thể hóa", "Đường lối hội nhập quốc tế"],
                        correct: 0,
                        hint: "Mở cửa kinh tế, đổi mới tư duy.",
                        explain: "Đại hội VI của Đảng (12/1986) phát động công cuộc Đổi Mới toàn diện, mở đường cho đất nước phát triển kinh tế thị trường định hướng XHCN."
                    },
                    {
                        q: "Anh hùng phi công Việt Nam nào đã bắn rơi máy bay B-52 của Mỹ rồi nhảy dù an toàn trong chiến dịch năm 1972?",
                        options: ["Phạm Tuân", "Nguyễn Văn Cừ", "Vũ Xuân Thiều", "Nguyen Văn Bảy"],
                        correct: 0,
                        hint: "Sau này là nhà vũ trụ đầu tiên của Việt Nam.",
                        explain: "Đêm 27/12/1972, phi công Phạm Tuân điều khiển MiG-21 bắn rơi máy bay B-52 trên bầu trời Hà Nội. Năm 1980 ông là người Việt Nam đầu tiên bay vào vũ trụ."
                    },
                    {
                        q: "Đội nữ du kích lái xe đường Trường Sơn kiên cường trong kháng chiến chống Mỹ có tên gọi là gì?",
                        options: ["Đội nữ lái xe Nguyễn Thị Hạnh", "Đội nữ lái xe Trung đoàn 559", "Đội nữ du kích Bến Tre", "Đội thanh niên xung phong Đồng Lộc"],
                        correct: 1,
                        hint: "Vận chuyển lương thực, đạn dược qua đèo hiểm trở.",
                        explain: "Đội nữ lái xe đường Trường Sơn gồm các cô gái tuổi đời rất trẻ vận chuyển vũ khí đạn dược vượt mìn bom chi viện miền Nam."
                    },
                    {
                        q: "10 cô gái thanh niên xung phong đã dũng cảm hy sinh tại ngã ba giao thông huyết mạch nào trên đường Trường Sơn năm 1968?",
                        options: ["Ngã ba Đồng Lộc (Hà Tĩnh)", "Hang Tám Cô (Quảng Bình)", "Truông Bồn (Nghệ An)", "Đèo Đá Bẽo"],
                        correct: 0,
                        hint: "Tiểu đội 4 do Võ Thị Qin làm Tiểu đội trưởng.",
                        explain: "Ngày 24/7/1968, 10 nữ thanh niên xung phong tại Ngã ba Đồng Lộc (Hà Tĩnh) do Võ Thị Qin làm tiểu đội trưởng đã anh dũng hy sinh khi san lấp hố bom."
                    },
                    {
                        q: "Năm 1995, Việt Nam đạt được mốc ngoại giao quan trọng nào đánh dấu hội nhập khu vực và thế giới?",
                        options: ["Gia nhập ASEAN và bình thường hóa quan hệ với Hoa Kỳ", "Gia nhập WTO", "Gia nhập Liên Hợp Quốc", "Ký hiệp định CPTPP"],
                        correct: 0,
                        hint: "Tháng 7 năm 1995.",
                        explain: "Tháng 7/1995, Việt Nam chính thức bình thường hóa quan hệ ngoại giao với Hoa Kỳ và gia nhập Hiệp hội các quốc gia Đông Nam Á (ASEAN)."
                    }
                ]
            }
        ];

        // --- GAME STATE ---
        let userProgress = JSON.parse(localStorage.getItem('vn_history_quiz_6lvl')) || {
            unlockedLevel: 1,
            stars: { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0 }
        };

        let currentLevelObj = null;
        let currentQIndex = 0;
        let currentScore = 0;
        let streak = 0;
        let timerInterval = null;
        let timeLeft = 0;
        let correctCount = 0;
        let isAnswered = false;

        // --- NAVIGATION LOGIC ---
        function returnToCover() {
            playSound('click');
            hideAllScreens();
            document.getElementById('mainCover').classList.remove('hidden');
            updateTotalStarsUI();
        }

        function goToLevelSelect() {
            playSound('click');
            hideAllScreens();
            renderLevelCards();
            document.getElementById('levelSelectScreen').classList.remove('hidden');
        }

        function hideAllScreens() {
            document.getElementById('mainCover').classList.add('hidden');
            document.getElementById('levelSelectScreen').classList.add('hidden');
            document.getElementById('gameScreen').classList.add('hidden');
            document.getElementById('resultModal').classList.add('hidden');
        }

        function updateTotalStarsUI() {
            const totalStars = Object.values(userProgress.stars).reduce((a, b) => a + b, 0);
            document.getElementById('totalStarsCount').innerText = `Tổng Sao: ${totalStars}/18`;
        }

        // --- RENDER 6 LEVEL CARDS ---
        function renderLevelCards() {
            const grid = document.getElementById('levelsGrid');
            grid.innerHTML = '';

            levelsData.forEach(lvl => {
                const isUnlocked = lvl.id <= userProgress.unlockedLevel;
                const starsCount = userProgress.stars[lvl.id] || 0;

                const card = document.createElement('div');
                card.className = `level-card ancient-border p-5 rounded-xl bg-stone-900/90 relative flex flex-col justify-between ${isUnlocked ? 'cursor-pointer hover:border-amber-400' : 'opacity-60 locked bg-stone-950'}`;
                
                let starsHTML = '';
                for (let i = 1; i <= 3; i++) {
                    starsHTML += `<i class="fa-solid fa-star ${i <= starsCount ? 'text-amber-400' : 'text-stone-700'} text-xs"></i>`;
                }

                card.innerHTML = `
                    <div>
                        <div class="flex justify-between items-start mb-2">
                            <span class="w-9 h-9 rounded-full bg-amber-950 border border-amber-600 flex items-center justify-center text-amber-400 text-sm">
                                <i class="fa-solid ${lvl.icon}"></i>
                            </span>
                            <div class="flex space-x-1 bg-stone-950/80 px-2 py-1 rounded-full border border-stone-800">${starsHTML}</div>
                        </div>
                        <h3 class="font-title text-sm md:text-base font-bold text-amber-200 mb-1 leading-snug">${lvl.title}</h3>
                        <p class="text-xs text-stone-400 mb-3">${lvl.desc}</p>
                    </div>

                    <div class="pt-3 border-t border-amber-900/40 flex justify-between items-center text-xs">
                        <span class="text-amber-500 font-semibold"><i class="fa-regular fa-clock mr-1"></i>${lvl.timeLimit}s/câu</span>
                        ${isUnlocked ? 
                            `<span class="px-3 py-1 bg-amber-600 hover:bg-amber-500 text-stone-950 font-bold rounded-md transition-colors">VÀO CHƠI</span>` : 
                            `<span class="text-stone-500 font-bold"><i class="fa-solid fa-lock mr-1"></i>Chưa mở</span>`
                        }
                    </div>
                `;

                if (isUnlocked) {
                    card.onclick = () => startQuiz(lvl);
                }

                grid.appendChild(card);
            });
        }

        // --- QUIZ LOGIC ---
        function startQuiz(lvl) {
            playSound('click');
            currentLevelObj = lvl;
            currentQIndex = 0;
            currentScore = 0;
            streak = 0;
            correctCount = 0;

            document.getElementById('levelBadge').innerText = `LEVEL ${lvl.id}`;
            document.getElementById('scoreText').innerText = '0';
            
            // Reset lifelines & displays
            document.getElementById('btnFifty').disabled = false;
            document.getElementById('btnHint').disabled = false;
            document.getElementById('btnAudience').disabled = false;
            document.getElementById('lifelineDisplay').classList.add('hidden');
            document.getElementById('explanationBox').classList.add('hidden');

            hideAllScreens();
            document.getElementById('gameScreen').classList.remove('hidden');
            loadQuestion();
        }

        function loadQuestion() {
            isAnswered = false;
            const q = currentLevelObj.questions[currentQIndex];
            
            document.getElementById('qCounter').innerText = `Câu ${currentQIndex + 1}/${currentLevelObj.questions.length}`;
            document.getElementById('questionText').innerText = q.q;
            document.getElementById('lifelineDisplay').classList.add('hidden');
            document.getElementById('explanationBox').classList.add('hidden');

            // Render 4 Options
            const grid = document.getElementById('optionsGrid');
            grid.innerHTML = '';
            q.options.forEach((opt, idx) => {
                const btn = document.createElement('button');
                btn.id = `opt-${idx}`;
                btn.className = "w-full p-3 rounded-xl bg-stone-800/90 border border-amber-700/60 hover:border-amber-400 hover:bg-amber-950/50 text-amber-100 font-medium text-left transition-all duration-150 flex items-center space-x-3 group cursor-pointer";
                btn.onclick = () => handleAnswer(idx, btn);
                btn.innerHTML = `
                    <span class="w-6 h-6 rounded-full bg-amber-900/60 border border-amber-600/80 text-amber-300 font-bold text-xs flex items-center justify-center shrink-0 group-hover:bg-amber-600 group-hover:text-stone-950">
                        ${String.fromCharCode(65 + idx)}
                    </span>
                    <span class="flex-1 text-xs md:text-sm leading-tight">${opt}</span>
                `;
                grid.appendChild(btn);
            });

            startTimer();
        }

        function startTimer() {
            clearInterval(timerInterval);
            timeLeft = currentLevelObj.timeLimit;
            const circle = document.getElementById('timerCircle');
            const timerText = document.getElementById('timerText');
            
            const maxDash = 107; // 2 * PI * r (r=17)
            circle.style.strokeDashoffset = 0;
            circle.setAttribute('stroke', '#f59e0b');
            timerText.innerText = timeLeft;

            timerInterval = setInterval(() => {
                timeLeft--;
                timerText.innerText = timeLeft;
                
                const offset = maxDash - (timeLeft / currentLevelObj.timeLimit) * maxDash;
                circle.style.strokeDashoffset = offset;

                if (timeLeft <= 4) {
                    circle.setAttribute('stroke', '#ef4444');
                }

                if (timeLeft <= 0) {
                    clearInterval(timerInterval);
                    handleTimeout();
                }
            }, 1000);
        }

        function handleAnswer(selectedIndex, buttonEl) {
            if (isAnswered) return;
            isAnswered = true;
            clearInterval(timerInterval);

            const q = currentLevelObj.questions[currentQIndex];
            const allBtns = document.querySelectorAll('#optionsGrid button');
            allBtns.forEach(b => b.onclick = null);

            // Show explanation
            document.getElementById('explanationText').innerText = q.explain;
            document.getElementById('explanationBox').classList.remove('hidden');

            if (selectedIndex === q.correct) {
                playSound('correct');
                buttonEl.classList.remove('bg-stone-800/90', 'border-amber-700/60');
                buttonEl.classList.add('bg-emerald-900/90', 'border-emerald-500', 'text-emerald-200');
                
                streak++;
                correctCount++;
                const bonus = streak > 1 ? (streak - 1) * 15 : 0;
                const earned = 100 + bonus + timeLeft * 4;
                currentScore += earned;

                document.getElementById('scoreText').innerText = currentScore;
                
                if (streak > 1) {
                    document.getElementById('streakNum').innerText = streak;
                    document.getElementById('streakBadge').classList.remove('hidden');
                }
            } else {
                playSound('wrong');
                buttonEl.classList.remove('bg-stone-800/90', 'border-amber-700/60');
                buttonEl.classList.add('bg-rose-950/90', 'border-rose-600', 'text-rose-200');
                
                // Highlight correct
                allBtns[q.correct].classList.add('bg-emerald-900/70', 'border-emerald-500');
                streak = 0;
                document.getElementById('streakBadge').classList.add('hidden');
            }

            setTimeout(nextQuestion, 3200);
        }

        function handleTimeout() {
            if (isAnswered) return;
            isAnswered = true;
            playSound('wrong');
            
            const q = currentLevelObj.questions[currentQIndex];
            const allBtns = document.querySelectorAll('#optionsGrid button');
            allBtns.forEach(b => b.onclick = null);
            allBtns[q.correct].classList.add('bg-emerald-900/70', 'border-emerald-500');

            document.getElementById('explanationText').innerText = q.explain;
            document.getElementById('explanationBox').classList.remove('hidden');
            
            streak = 0;
            document.getElementById('streakBadge').classList.add('hidden');
            setTimeout(nextQuestion, 3200);
        }

        function nextQuestion() {
            currentQIndex++;
            if (currentQIndex < currentLevelObj.questions.length) {
                loadQuestion();
            } else {
                finishQuiz();
            }
        }

        // --- POWER-UP HELPLINES ---
        function useFiftyFifty() {
            if (isAnswered) return;
            playSound('click');
            document.getElementById('btnFifty').disabled = true;

            const q = currentLevelObj.questions[currentQIndex];
            let wrongIndices = [];
            q.options.forEach((_, idx) => {
                if (idx !== q.correct) wrongIndices.push(idx);
            });

            wrongIndices.sort(() => Math.random() - 0.5);
            wrongIndices.slice(0, 2).forEach(idx => {
                const btn = document.getElementById(`opt-${idx}`);
                if (btn) btn.classList.add('opacity-20', 'pointer-events-none');
            });
        }

        function useHint() {
            if (isAnswered) return;
            playSound('click');
            document.getElementById('btnHint').disabled = true;
            const q = currentLevelObj.questions[currentQIndex];
            document.getElementById('lifelineText').innerHTML = `<i class="fa-regular fa-lightbulb text-amber-400 mr-1"></i> <strong>Gợi ý:</strong> ${q.hint}`;
            document.getElementById('lifelineDisplay').classList.remove('hidden');
        }

        function useAudience() {
            if (isAnswered) return;
            playSound('click');
            document.getElementById('btnAudience').disabled = true;
            const q = currentLevelObj.questions[currentQIndex];
            
            let percents = [15, 15, 15, 15];
            percents[q.correct] += 40;
            // randomize remaining
            percents = percents.map(p => Math.floor(p + Math.random() * 10));
            
            const text = percents.map((p, i) => `${String.fromCharCode(65 + i)}: ${p}%`).join(' | ');
            document.getElementById('lifelineText').innerHTML = `<i class="fa-solid fa-users text-amber-400 mr-1"></i> <strong>Ý kiến khán giả:</strong> ${text}`;
            document.getElementById('lifelineDisplay').classList.remove('hidden');
        }

        function exitQuiz() {
            playSound('click');
            clearInterval(timerInterval);
            goToLevelSelect();
        }

        // --- FINISH QUIZ & RESULT CALCULATIONS ---
        function finishQuiz() {
            clearInterval(timerInterval);
            const totalQ = currentLevelObj.questions.length; // 15
            const ratio = correctCount / totalQ;

            let earnedStars = 0;
            if (correctCount >= 14) earnedStars = 3;
            else if (correctCount >= 11) earnedStars = 2;
            else if (correctCount >= 8) earnedStars = 1;

            // Save Progress
            if (earnedStars > (userProgress.stars[currentLevelObj.id] || 0)) {
                userProgress.stars[currentLevelObj.id] = earnedStars;
            }

            // Unlock next level if passed with >= 1 star (at least 8/15 correct)
            if (earnedStars >= 1 && currentLevelObj.id === userProgress.unlockedLevel && currentLevelObj.id < levelsData.length) {
                userProgress.unlockedLevel = currentLevelObj.id + 1;
            }

            localStorage.setItem('vn_history_quiz_6lvl', JSON.stringify(userProgress));

            // UI Result Modal Display
            document.getElementById('resCorrect').innerText = `${correctCount}/${totalQ}`;
            document.getElementById('resScore').innerText = currentScore;
            
            const starIcons = document.querySelectorAll('#starContainer i');
            starIcons.forEach((star, i) => {
                if (i < earnedStars) {
                    star.className = 'fa-solid fa-star text-amber-400 transform scale-110 drop-shadow-[0_0_8px_rgba(245,158,11,0.8)]';
                } else {
                    star.className = 'fa-solid fa-star text-stone-700';
                }
            });

            const statusEl = document.getElementById('resStatus');
            if (earnedStars >= 1) {
                playSound('win');
                document.getElementById('resultTitle').innerText = "CHIẾN THẮNG MÀN CHƠI!";
                statusEl.innerText = "Đã thông qua (Mở khóa màn mới)";
                statusEl.className = "text-emerald-400 font-bold";
            } else {
                playSound('wrong');
                document.getElementById('resultTitle').innerText = "CHƯA ĐẠT YÊU CẦU";
                statusEl.innerText = "Cần đúng từ 8/15 câu để qua màn";
                statusEl.className = "text-rose-400 font-bold";
            }

            const btnNext = document.getElementById('btnNextLevel');
            if (currentLevelObj.id < levelsData.length && earnedStars >= 1) {
                btnNext.classList.remove('hidden');
            } else {
                btnNext.classList.add('hidden');
            }

            document.getElementById('resultModal').classList.remove('hidden');
        }

        function nextLevelAction() {
            const nextLvl = levelsData.find(l => l.id === currentLevelObj.id + 1);
            if (nextLvl) {
                startQuiz(nextLvl);
            } else {
                goToLevelSelect();
            }
        }

        // --- SETTINGS LOGIC ---
        function openSettings() {
            playSound('click');
            document.getElementById('settingsModal').classList.remove('hidden');
        }

        function closeSettings() {
            playSound('click');
            document.getElementById('settingsModal').classList.add('hidden');
        }

        function updateSettings() {
            isSoundEnabled = document.getElementById('sfxToggle').checked;
        }

        function resetProgress() {
            if (confirm("Bạn có chắc chắn muốn xóa toàn bộ tiến trình và reset về Level 1?")) {
                userProgress = { unlockedLevel: 1, stars: { 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0 } };
                localStorage.setItem('vn_history_quiz_6lvl', JSON.stringify(userProgress));
                closeSettings();
                goToLevelSelect();
            }
        }

        // --- BACKGROUND PARTICLES ON LOAD ---
        window.onload = function() {
            updateTotalStarsUI();

            const canvas = document.getElementById('particleCanvas');
            const ctx = canvas.getContext('2d');
            let width = canvas.width = window.innerWidth;
            let height = canvas.height = window.innerHeight;

            window.addEventListener('resize', () => {
                width = canvas.width = window.innerWidth;
                height = canvas.height = window.innerHeight;
            });

            const particles = Array.from({ length: 40 }, () => ({
                x: Math.random() * width,
                y: Math.random() * height,
                radius: Math.random() * 2 + 0.5,
                color: `rgba(245, 158, 11, ${Math.random() * 0.5 + 0.2})`,
                vx: (Math.random() - 0.5) * 0.4,
                vy: -Math.random() * 0.5 - 0.2
            }));

            function animateParticles() {
                ctx.clearRect(0, 0, width, height);
                particles.forEach(p => {
                    p.x += p.vx;
                    p.y += p.vy;
                    if (p.y < 0) {
                        p.y = height;
                        p.x = Math.random() * width;
                    }
                    if (p.x < 0 || p.x > width) p.vx *= -1;

                    ctx.beginPath();
                    ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
                    ctx.fillStyle = p.color;
                    ctx.shadowBlur = 6;
                    ctx.shadowColor = '#f59e0b';
                    ctx.fill();
                });
                requestAnimationFrame(animateParticles);
            }

            animateParticles();
        };
    </script>
</body>
</html>
