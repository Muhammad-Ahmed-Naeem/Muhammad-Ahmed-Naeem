import os

def create_svg(theme):
    if theme == 'dark':
        bg = "#030712"
        panel_bg = "rgba(15, 23, 42, 0.7)"
        border = "rgba(255, 255, 255, 0.08)"
        text_primary = "#F8FAFC"
        text_secondary = "#94A3B8"
        accent_1 = "#7C3AED"
        accent_2 = "#22D3EE"
        accent_3 = "#10B981"
        ascii_grad_1 = "#06B6D4"
        ascii_grad_2 = "#7C3AED"
        glow_colors = ["#2563EB", "#7C3AED", "#10B981"]
    else:
        bg = "#FFFFFF"
        panel_bg = "rgba(248, 250, 252, 0.85)"
        border = "rgba(15, 23, 42, 0.08)"
        text_primary = "#0F172A"
        text_secondary = "#475569"
        accent_1 = "#2563EB"
        accent_2 = "#06B6D4"
        accent_3 = "#10B981"
        ascii_grad_1 = "#2563EB"
        ascii_grad_2 = "#06B6D4"
        glow_colors = ["#93C5FD", "#C4B5FD", "#6EE7B7"]

    ascii_portrait = [
        "                 ......                 ",
        "            .,:;iiiiiiiii;:,.           ",
        "         .,;iiiiiiiiiiiiiiiii;,.        ",
        "       .,iiiiiiiiiiiiiiiiiiiiiii,.      ",
        "      ,iiiiiiiiiiiiiiiiiiiiiiiiiii,     ",
        "     ,iiiiiiiiiiiiiiiiiiiiiiiiiiiii,    ",
        "    ,iiiiiiiiiiiiiiiiiiiiiiiiiiiiiii,   ",
        "    ;iiiiiiiiiiiiiiiiiiiiiiiiiiiiiii;   ",
        "    ;iiiiiiiii:;;iiiiiii;;:iiiiiiiii;   ",
        "    ;iiiiiii;..   .iii.   ..;iiiiiii;   ",
        "    :iiiiiii:      .i.      :iiiiiii:   ",
        "    .iiiiiii, |X|  .i.  |X| ,iiiiiii.   ",
        "     :iiiii,   _   .i.   _   ,iiiii:    ",
        "      ;iiiii:,....,iii,....,:iiiii;     ",
        "       ,iiiiiiiiiiiiiiiiiiiiiiiii,      ",
        "         ,iiiiii;:iiiii:;iiiiii,        ",
        "           .,:;iii;;;;;iii;:,.          ",
        "              ..,,:::::,,..             ",
        "        .,:;iiiiiiiiiiiiiiiii;:,.       ",
        "     .,;iiiiiiiiiiiiiiiiiiiiiiiii;,.    ",
        "   .,iiiiiiiiiiiiiiiiiiiiiiiiiiiiiii,.  ",
        "  ,iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii, "
    ]

    # Skills removed as requested

    # Generate ASCII SVG
    ascii_svg = ""
    for i, line in enumerate(ascii_portrait):
        y_pos = 80 + (i * 13)
        line = line.replace(" ", "&#160;")
        ascii_svg += f'<text x="240" y="{y_pos}" text-anchor="middle" font-family="monospace" font-size="13" fill="url(#asciiGrad)" font-weight="bold" letter-spacing="2">{line}</text>\n'

    # Add blinking cursor to ASCII
    cursor_y = 80 + (len(ascii_portrait) * 13)
    ascii_svg += f'''
    <text x="240" y="{cursor_y}" text-anchor="middle" font-family="monospace" font-size="13" fill="url(#asciiGrad)" font-weight="bold">_
        <animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite" />
    </text>
    '''

    socials = [
        # GitHub
        ("M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z", "https://github.com/Muhammad-Ahmed-Naeem"),
        # LinkedIn
        ("M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z", "https://linkedin.com"),
        # Twitter
        ("M18.901 1.153h3.68l-8.04 9.19L24 22.846h-7.406l-5.8-7.584-6.638 7.584H.474l8.6-9.83L0 1.154h7.594l5.243 6.932ZM17.61 20.644h2.039L6.486 3.24H4.298Z", "https://twitter.com"),
        # Mail
        ("M2 6a2 2 0 012-2h16a2 2 0 012 2v12a2 2 0 01-2 2H4a2 2 0 01-2-2V6zm2 0v.011l8 4.666 8-4.666V6H4zm16 2.083l-8 4.666-8-4.666V18h16V8.083z", "mailto:muhammad.ahmed.prof@gmail.com")
    ]
    
    socials_svg = ""
    soc_x = 490
    soc_delay = 2.8
    for path, link in socials:
        socials_svg += f'''
        <g opacity="0">
            <animate attributeName="opacity" values="0;1" dur="0.6s" begin="{soc_delay}s" fill="freeze" />
            <animateTransform attributeName="transform" type="translate" values="0, 10; 0, 0" dur="0.6s" begin="{soc_delay}s" fill="freeze" />
            <a href="{link}" target="_blank">
                <g class="icon" transform="translate({soc_x}, 340)">
                    <rect x="0" y="0" width="36" height="36" rx="8" fill="rgba(15,23,42,0.1)" stroke="{border}" />
                    <path d="{path}" transform="translate(6, 6) scale(1.0)" fill="{text_secondary}" />
                </g>
            </a>
        </g>'''
        soc_x += 46
        soc_delay += 0.15

    # Typing roles
    roles = [
        ("> Software Engineer", 240),
        ("> AI Enthusiast", 200),
        ("> Unreal Engine Dev", 260),
        ("> Game Developer", 220)
    ]
    
    typing_svg = ""
    dur = 16
    slot = 4 # Each role gets 4 seconds
    for i, (text, w) in enumerate(roles):
        # We need keyTimes for opacity: fade in, stay, fade out, stay hidden
        # i * 4 to (i+1) * 4
        start_ratio = (i * slot) / dur
        end_ratio = ((i + 1) * slot) / dur
        fade_in = start_ratio + 0.01
        fade_out = end_ratio - 0.01
        
        # Build keyTimes
        # e.g. for i=0: 0; 0.01; 0.24; 0.25; 1
        # for i=1: 0; 0.24; 0.25; 0.49; 0.50; 1
        k_times = f"0; {max(0, start_ratio - 0.01)}; {start_ratio}; {end_ratio}; {min(1, end_ratio + 0.01)}; 1"
        if i == 0:
            k_times = f"0; 0.01; {end_ratio}; {end_ratio + 0.01}; 1"
            op_vals = "1; 1; 1; 0; 0"
        elif i == len(roles) - 1:
            k_times = f"0; {start_ratio - 0.01}; {start_ratio}; 0.99; 1"
            op_vals = "0; 0; 1; 1; 1"
        else:
            op_vals = "0; 0; 1; 1; 0; 0"

        typing_svg += f'''
        <g opacity="0">
            <animate attributeName="opacity" values="{op_vals}" keyTimes="{k_times}" dur="{dur}s" repeatCount="indefinite" />
            <mask id="mask_role{i}">
                <rect x="490" y="150" width="300" height="40" fill="white">
                    <animate attributeName="width" values="0; {w}; {w}; 0" keyTimes="0; 0.3; 0.8; 1" dur="{slot}s" repeatCount="indefinite" />
                </rect>
            </mask>
            <text x="490" y="180" font-family="monospace" font-size="24" fill="url(#accentGrad)" mask="url(#mask_role{i})">{text}</text>
            <rect y="160" width="12" height="24" fill="{accent_2}">
                <animate attributeName="x" values="490; {490+w+5}; {490+w+5}; 490" keyTimes="0; 0.3; 0.8; 1" dur="{slot}s" repeatCount="indefinite" />
                <animate attributeName="opacity" values="1;0;1;0;1;0;1;0" dur="1s" repeatCount="indefinite" />
            </rect>
        </g>
        '''

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1180" height="440" viewBox="0 0 1180 440">
    <defs>
        <radialGradient id="glow1" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="{glow_colors[0]}" stop-opacity="0.3" />
            <stop offset="100%" stop-color="{glow_colors[0]}" stop-opacity="0" />
        </radialGradient>
        <radialGradient id="glow2" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="{glow_colors[1]}" stop-opacity="0.3" />
            <stop offset="100%" stop-color="{glow_colors[1]}" stop-opacity="0" />
        </radialGradient>
        <radialGradient id="glow3" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="{glow_colors[2]}" stop-opacity="0.3" />
            <stop offset="100%" stop-color="{glow_colors[2]}" stop-opacity="0" />
        </radialGradient>
        
        <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="{accent_1}">
                <animate attributeName="stop-color" values="{accent_1};{accent_2};{accent_3};{accent_1}" dur="8s" repeatCount="indefinite" />
            </stop>
            <stop offset="50%" stop-color="{accent_2}">
                <animate attributeName="stop-color" values="{accent_2};{accent_3};{accent_1};{accent_2}" dur="8s" repeatCount="indefinite" />
            </stop>
            <stop offset="100%" stop-color="{accent_3}">
                <animate attributeName="stop-color" values="{accent_3};{accent_1};{accent_2};{accent_3}" dur="8s" repeatCount="indefinite" />
            </stop>
        </linearGradient>

        <linearGradient id="asciiGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="{ascii_grad_1}">
                <animate attributeName="stop-color" values="{ascii_grad_1};{ascii_grad_2};{ascii_grad_1}" dur="6s" repeatCount="indefinite" />
            </stop>
            <stop offset="100%" stop-color="{ascii_grad_2}">
                <animate attributeName="stop-color" values="{ascii_grad_2};{ascii_grad_1};{ascii_grad_2}" dur="6s" repeatCount="indefinite" />
            </stop>
        </linearGradient>

        <linearGradient id="borderGlow" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stop-color="{border}" />
            <stop offset="50%" stop-color="{accent_1}" stop-opacity="0.8">
                <animate attributeName="offset" values="0; 1; 0" dur="5s" repeatCount="indefinite" />
            </stop>
            <stop offset="100%" stop-color="{border}" />
        </linearGradient>
        
        <filter id="noiseFilter">
            <feTurbulence type="fractalNoise" baseFrequency="0.75" stitchTiles="stitch"/>
            <feColorMatrix type="saturate" values="0" />
        </filter>

        <mask id="asciiReveal">
            <rect x="0" y="0" width="100%" height="0" fill="white">
                <animate attributeName="height" values="0; 100%" dur="3s" fill="freeze" />
            </rect>
        </mask>
        
        <!-- Clipping paths for rounded corners -->
        <clipPath id="panelClip1">
            <rect x="40" y="40" width="400" height="360" rx="20" />
        </clipPath>
        <clipPath id="panelClip2">
            <rect x="460" y="40" width="680" height="360" rx="20" />
        </clipPath>
    </defs>

    <style>
        .pill, .icon {{
            transform-box: fill-box;
            transform-origin: center;
        }}
        .pill-bg {{
            transition: all 0.3s ease;
        }}
        .pill:hover .pill-bg {{
            stroke: {accent_2};
            stroke-width: 2;
        }}
        .icon:hover rect {{
            stroke: {accent_2};
            stroke-width: 2;
            fill: rgba(15,23,42,0.3);
        }}
        @keyframes floatAscii {{
            0% {{ transform: translateY(0px); }}
            50% {{ transform: translateY(-10px); }}
            100% {{ transform: translateY(0px); }}
        }}
        .floating {{
            animation: floatAscii 6s ease-in-out infinite;
        }}
    </style>

    <!-- Main Background -->
    <rect width="100%" height="100%" fill="{bg}" rx="24" />
    
    <!-- Noise overlay -->
    <rect width="100%" height="100%" filter="url(#noiseFilter)" opacity="0.04" rx="24" style="mix-blend-mode: overlay;" />

    <!-- Animated Background Glows -->
    <g opacity="0.8">
        <circle cx="20%" cy="30%" r="300" fill="url(#glow1)">
            <animate attributeName="cy" values="30%; 40%; 30%" dur="12s" repeatCount="indefinite" />
            <animate attributeName="cx" values="20%; 25%; 20%" dur="15s" repeatCount="indefinite" />
        </circle>
        <circle cx="80%" cy="70%" r="400" fill="url(#glow2)">
            <animate attributeName="cy" values="70%; 60%; 70%" dur="14s" repeatCount="indefinite" />
            <animate attributeName="cx" values="80%; 75%; 80%" dur="18s" repeatCount="indefinite" />
        </circle>
        <circle cx="50%" cy="50%" r="250" fill="url(#glow3)">
            <animate attributeName="cy" values="50%; 45%; 50%" dur="10s" repeatCount="indefinite" />
        </circle>
    </g>

    <!-- Floating Particles -->
    <g fill="{accent_2}" opacity="0.4">
        <circle cx="100" cy="500" r="2">
            <animate attributeName="cy" values="500; 100" dur="15s" repeatCount="indefinite" />
            <animate attributeName="opacity" values="0; 0.4; 0" dur="15s" repeatCount="indefinite" />
        </circle>
        <circle cx="350" cy="450" r="1.5">
            <animate attributeName="cy" values="450; 50" dur="12s" repeatCount="indefinite" />
            <animate attributeName="opacity" values="0; 0.4; 0" dur="12s" repeatCount="indefinite" />
        </circle>
        <circle cx="800" cy="550" r="2">
            <animate attributeName="cy" values="550; 150" dur="18s" repeatCount="indefinite" />
            <animate attributeName="opacity" values="0; 0.4; 0" dur="18s" repeatCount="indefinite" />
        </circle>
        <circle cx="1050" cy="300" r="1.5">
            <animate attributeName="cy" values="300; 0" dur="10s" repeatCount="indefinite" />
            <animate attributeName="opacity" values="0; 0.4; 0" dur="10s" repeatCount="indefinite" />
        </circle>
    </g>

    <!-- Moving Scanline -->
    <rect width="100%" height="2" fill="{accent_2}" opacity="0.15">
        <animate attributeName="y" values="-10; 450; -10" dur="6s" repeatCount="indefinite" />
    </rect>

    <!-- LEFT PANEL (ASCII Portrait) -->
    <rect x="40" y="40" width="400" height="360" rx="20" fill="{panel_bg}" stroke="url(#borderGlow)" stroke-width="1.5" />
    <g clip-path="url(#panelClip1)">
        <!-- Inner glass shadow/reflection -->
        <rect x="40" y="40" width="400" height="30" fill="white" opacity="0.03" />
        
        <!-- The ASCII Portrait -->
        <g class="floating" mask="url(#asciiReveal)">
            {ascii_svg}
        </g>
    </g>

    <!-- RIGHT PANEL (Terminal) -->
    <rect x="460" y="40" width="680" height="360" rx="20" fill="{panel_bg}" stroke="url(#borderGlow)" stroke-width="1.5" />
    <g clip-path="url(#panelClip2)">
        <!-- Terminal Top Bar -->
        <rect x="460" y="40" width="680" height="40" fill="rgba(0,0,0,0.2)" />
        <circle cx="490" cy="60" r="6" fill="#EF4444" />
        <circle cx="515" cy="60" r="6" fill="#F59E0B" />
        <circle cx="540" cy="60" r="6" fill="#10B981" />
        <text x="565" y="64" fill="{text_secondary}" font-family="monospace" font-size="12">~/portfolio/readme.sh</text>
        
        <!-- Greeting -->
        <g opacity="0">
            <animate attributeName="opacity" values="0;1" dur="1s" begin="0.5s" fill="freeze" />
            <animateTransform attributeName="transform" type="translate" values="0, 10; 0, 0" dur="1s" begin="0.5s" fill="freeze" />
            <text x="490" y="130" fill="{text_primary}" font-family="sans-serif" font-weight="bold" font-size="34">Hi 👋 I'm Muhammad Ahmed Naeem</text>
        </g>

        <!-- Typing Text -->
        {typing_svg}

        <!-- Bio Items -->
        <g font-family="sans-serif" font-size="16" fill="{text_secondary}">
            <g opacity="0">
                <animate attributeName="opacity" values="0;1" dur="0.5s" begin="1.2s" fill="freeze" />
                <animateTransform attributeName="transform" type="translate" values="490, 240; 490, 230" dur="0.5s" begin="1.2s" fill="freeze" />
                <text x="0" y="0">🎓 Education:</text>
                <text x="110" y="0" fill="{text_primary}">Software Engineering</text>
            </g>
            <g opacity="0">
                <animate attributeName="opacity" values="0;1" dur="0.5s" begin="1.4s" fill="freeze" />
                <animateTransform attributeName="transform" type="translate" values="490, 275; 490, 265" dur="0.5s" begin="1.4s" fill="freeze" />
                <text x="0" y="0">🔭 Focus:</text>
                <text x="110" y="0" fill="{text_primary}">AI, Unreal Engine, Game Dev</text>
            </g>
            <g opacity="0">
                <animate attributeName="opacity" values="0;1" dur="0.5s" begin="1.6s" fill="freeze" />
                <animateTransform attributeName="transform" type="translate" values="490, 310; 490, 300" dur="0.5s" begin="1.6s" fill="freeze" />
                <text x="0" y="0">🌍 Portfolio:</text>
                <text x="110" y="0" fill="{text_primary}">github.com/Muhammad-Ahmed-Naeem</text>
            </g>
        </g>

        <!-- Social Icons -->
        {socials_svg}
        
    </g>

</svg>'''
    
    with open(f"{theme}.svg", "w", encoding="utf-8") as f:
        f.write(svg)

create_svg('dark')
create_svg('light')
print("Generated SVGs")
