def help():
    print()
    print("Tweaktron v0.0.1")
    print("Usage:")
    print("    tweaktron <command>")
    print("Commands:")
    print("    help                    displays this help menu")
    print("    set-timezone            sets the timezone")
    print("    configure-perf-overlay  configures the performance overlay (MangoHUD)")
    print("    set-fps-limit           sets a framerate limit")
    print("    enable-flatpak          enables flatpak")
    print("    set-resolution          sets the internal gamescope resolution - this resolution will be scaled to fit the display")
    print("    reset                   discards all changes made by Tweaktron")
    print("    reboot                  reboots the system")
    print()

if __name__ == "__main__":
    help()
