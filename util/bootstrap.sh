# Install image for android simulator and creates virtual device based on downloaded image
# if ran with option run, runs emulator with auto detected gpu acceleration (better check this option in Android Studio)

#$ANDROID_HOME/tools/bin/sdkmanager "system-images;android-23;google_apis;x86"
#$ANDROID_HOME/tools/bin/avdmanager --verbose create avd  -c 100M --force --name test --device "Nexus 5X" --package "system-images;android-23;google_apis;x86" --tag "google_apis" --abi "x86"
if  [[ $1 = "-run" ]]; then
    $ANDROID_HOME/tools/emulator @test -gpu auto
fi

