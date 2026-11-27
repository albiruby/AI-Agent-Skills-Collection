#!/usr/bin/env python3
"""Scaffold a production-ready Garmin Connect IQ project."""

import argparse
import os
import uuid


def main() -> None:
    parser = argparse.ArgumentParser(description="Scaffold a Garmin Connect IQ project.")
    parser.add_argument("--name", required=True, help="Project/Class prefix name (e.g. BioFeeder)")
    parser.add_argument(
        "--type",
        default="watchface",
        choices=["watchface", "datafield", "watch-app", "widget", "audio-content-provider"],
        help="Connect IQ application type",
    )
    parser.add_argument("--out", required=True, help="Output directory path")
    args = parser.parse_args()

    out_dir = os.path.abspath(args.out)
    os.makedirs(os.path.join(out_dir, "source"), exist_ok=True)
    os.makedirs(os.path.join(out_dir, "resources", "strings"), exist_ok=True)
    os.makedirs(os.path.join(out_dir, "resources", "drawables"), exist_ok=True)

    app_uuid = str(uuid.uuid4())
    app_class = f"{args.name}App"
    view_class = f"{args.name}View"

    manifest = f"""<?xml version="1.0"?>
<iq:manifest xmlns:iq="http://www.garmin.com/xml/connectiq" version="3">
    <iq:application id="{app_uuid}"
                    type="{args.type}"
                    name="@Strings.AppName"
                    entry="{app_class}"
                    launcherIcon="@Drawables.LauncherIcon"
                    minApiLevel="3.2.0">
        <iq:products>
            <iq:product id="fenix7"/>
            <iq:product id="epix2"/>
            <iq:product id="fr265"/>
            <iq:product id="fr965"/>
            <iq:product id="venu3"/>
        </iq:products>
        <iq:permissions/>
        <iq:languages>
            <iq:language>eng</iq:language>
        </iq:languages>
        <iq:barrels/>
    </iq:application>
</iq:manifest>
"""
    with open(os.path.join(out_dir, "manifest.xml"), "w") as f:
        f.write(manifest)

    with open(os.path.join(out_dir, "monkey.jungle"), "w") as f:
        f.write("project.manifest = manifest.xml\nbase.sourcePath = source\nbase.resourcePath = resources\n")

    with open(os.path.join(out_dir, "resources", "strings", "strings.xml"), "w") as f:
        f.write(f'<strings>\n    <string id="AppName">{args.name}</string>\n</strings>\n')

    app_mc = f"""import Toybox.Application;
import Toybox.Lang;
import Toybox.WatchUi;

class {app_class} extends Application.AppBase {{
    public function initialize() {{
        AppBase.initialize();
    }}

    public function getInitialView() as [Views] or [Views, InputDelegates] {{
        return [new {view_class}()];
    }}
}}
"""
    with open(os.path.join(out_dir, "source", f"{app_class}.mc"), "w") as f:
        f.write(app_mc)

    print(f"Scaffolded Connect IQ {args.type} project at {out_dir} (UUID: {app_uuid})")


if __name__ == "__main__":
    main()
