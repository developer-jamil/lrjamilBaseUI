# JamilBaseUI

[![Release](https://jitpack.io/v/developer-jamil/JamilBaseUI.svg)](https://jitpack.io/#developer-jamil/JamilBaseUI)

A professional Android UI resource library for building fully responsive and scalable layouts across mobile, 7-inch tablets, and 10-inch tablets.

## Features
- **1000+ Responsive Dimensions:** Ready-to-use dimensions from `1sdp` to `500sdp` (including negative values).
- **Auto-Scaling Logic:** 
  - Standard scale for mobile.
  - **1.3x** scale for 7-inch tablets (`sw600dp`).
  - **1.5x** scale for 10-inch tablets (`sw720dp`).
- **Global Theme System:** Pre-defined styles for `TextView` (Headers, Bold, Medium, Small), `EditText`, and `CardView`.
- **Standardized Colors:** Clean, branding-ready color palette.

---

## Installation

### Step 1: Add the JitPack repository to your root `settings.gradle`
```gradle
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        mavenCentral()
        maven { url 'https://jitpack.io' }
    }
}
```

### Step 2: Add the dependency to your app's `build.gradle`
```gradle
dependencies {
    implementation 'com.github.developer-jamil:JamilBaseUI:v1.0.4'
}
```

---

## Usage

### 1. Using Scalable Dimensions
Instead of `dp`, use `@dimen/_{value}sdp`:

```xml
<TextView
    android:layout_width="@dimen/_200sdp"
    android:layout_height="@dimen/_50sdp"
    android:padding="@dimen/_10sdp"
    android:text="Responsive Text" />
```

Negative dimensions are also supported:
```xml
<ImageView
    android:layout_marginTop="@dimen/_minus20sdp"
    ... />
```

### 2. Using Global Styles
Apply professional styles to your views instantly:

```xml
<!-- Header Style -->
<TextView
    style="@style/header_1"
    android:text="Welcome Back" />

<!-- Normal Bold Text -->
<TextView
    style="@style/normal_text_bold"
    android:text="Login to your account" />

<!-- Standard EditText -->
<EditText
    style="@style/editTextStyle"
    android:hint="Email Address" />
```

---

## Technical Details
- **Min SDK:** 23
- **Compiled SDK:** 36
- **Version:** v1.0.4

## Developed By
**Jamil Lab LTD**
