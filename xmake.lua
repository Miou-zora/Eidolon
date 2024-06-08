add_rules("mode.debug", "mode.release")

target("Client")
    set_rundir(".")
    set_languages("c99")
    add_files("client/main.c")

    add_cflags("-Wall", "-Wextra")
    add_cflags("-Werror=vla-larger-than=0")
    add_cflags("-Wcast-qual", "-Wconversion")

    add_cflags("-Wmissing-prototypes")
    add_cflags("-Wstrict-prototypes")
    add_cflags("-Wshadow")
    add_cflags("-Wwrite-strings")

    if is_plat("windows") then
        add_syslinks("user32")
    end

    if is_mode("debug") then
        set_symbols("debug")
        set_optimize("none")
    end

    if is_mode("release") then
        set_symbols("hidden")
        set_optimize("fastest")
        set_strip("all")

    end

target("Server")
    set_rundir(".")
    set_languages("c99")
    add_files("server/main.c")

    add_cflags("-Wall", "-Wextra")
    add_cflags("-Werror=vla-larger-than=0")
    add_cflags("-Wcast-qual", "-Wconversion")

    add_cflags("-Wmissing-prototypes")
    add_cflags("-Wstrict-prototypes")
    add_cflags("-Wshadow")
    add_cflags("-Wwrite-strings")

    if is_plat("windows") then
        add_syslinks("user32")
    end

    if is_mode("debug") then
        set_symbols("debug")
        set_optimize("none")
    end

    if is_mode("release") then
        set_symbols("hidden")
        set_optimize("fastest")
        set_strip("all")
    end
