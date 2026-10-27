# Plant Disease Classes (subset of PlantVillage dataset)
# Optimized for high precision across common agricultural crops
CLASS_NAMES = [
    "Apple___Apple_scab",
    "Apple___Black_rot",
    "Apple___Cedar_apple_rust",
    "Apple___healthy",
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
    "Corn_(maize)___Common_rust_",
    "Corn_(maize)___Northern_Leaf_Blight",
    "Corn_(maize)___healthy",
    "Grape___Black_rot",
    "Grape___Esca_(Black_Measles)",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
    "Grape___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Tomato___Bacterial_spot",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites Two-spotted_spider_mite",
    "Tomato___Target_Spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato___Tomato_mosaic_virus",
    "Tomato___healthy"
]

DISEASE_INFO = {
    "Apple___Apple_scab": {
        "crop": "Apple",
        "condition": "Apple Scab",
        "severity": "Moderate",
        "recommendation": "Apply fungicide (Captan, Mancozeb) at green tip stage. Rake and dispose of fallen leaves to prevent spore overwintering."
    },
    "Apple___Black_rot": {
        "crop": "Apple",
        "condition": "Black Rot",
        "severity": "High",
        "recommendation": "Prune out dead or infected branches. Remove mummified fruit from trees and ground."
    },
    "Apple___Cedar_apple_rust": {
        "crop": "Apple",
        "condition": "Cedar Apple Rust",
        "severity": "Moderate",
        "recommendation": "Remove nearby eastern red cedar trees if possible. Apply preventative copper or sulfur fungicides early spring."
    },
    "Apple___healthy": {
        "crop": "Apple",
        "condition": "Healthy",
        "severity": "None",
        "recommendation": "Leaf is healthy. Continue balanced watering, fertilization, and routine orchard monitoring."
    },
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "crop": "Corn (Maize)",
        "condition": "Gray Leaf Spot",
        "severity": "Moderate to High",
        "recommendation": "Rotate crops and use disease-tolerant hybrid seeds. Apply strobilurin or triazole fungicides if lesions appear early."
    },
    "Corn_(maize)___Common_rust_": {
        "crop": "Corn (Maize)",
        "condition": "Common Rust",
        "severity": "Moderate",
        "recommendation": "Plant rust-resistant hybrids. Fungicide application is usually only warranted in seed production fields."
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "crop": "Corn (Maize)",
        "condition": "Northern Leaf Blight",
        "severity": "High",
        "recommendation": "Manage crop residue through tillage or rotation. Apply foliar fungicides if disease threatens ear leaf."
    },
    "Corn_(maize)___healthy": {
        "crop": "Corn (Maize)",
        "condition": "Healthy",
        "severity": "None",
        "recommendation": "Corn leaf is healthy. Ensure adequate nitrogen and moisture during silking."
    },
    "Grape___Black_rot": {
        "crop": "Grape",
        "condition": "Black Rot",
        "severity": "High",
        "recommendation": "Apply myclobutanil or mancozeb sprays starting at early shoot growth. Ensure good canopy aeration."
    },
    "Grape___Esca_(Black_Measles)": {
        "crop": "Grape",
        "condition": "Esca (Black Measles)",
        "severity": "High",
        "recommendation": "Prune during dry weather to prevent wound infection. Treat large pruning cuts with wound sealants."
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "crop": "Grape",
        "condition": "Leaf Blight",
        "severity": "Moderate",
        "recommendation": "Use copper-based fungicide spray post-harvest and ensure proper trellis air circulation."
    },
    "Grape___healthy": {
        "crop": "Grape",
        "condition": "Healthy",
        "severity": "None",
        "recommendation": "Vineyard foliage is healthy. Maintain pruning and balanced canopy sun exposure."
    },
    "Potato___Early_blight": {
        "crop": "Potato",
        "condition": "Early Blight",
        "severity": "Moderate",
        "recommendation": "Maintain optimal nitrogen levels. Apply chlorothalonil or azoxystrobin at initial sign of spotting."
    },
    "Potato___Late_blight": {
        "crop": "Potato",
        "condition": "Late Blight",
        "severity": "Critical",
        "recommendation": "Urgent treatment needed: apply systemic fungicides (metalaxyl/mancozeb). Destroy severely infected vines to protect tubers."
    },
    "Potato___healthy": {
        "crop": "Potato",
        "condition": "Healthy",
        "severity": "None",
        "recommendation": "Potato foliage is healthy. Maintain hilling and avoid overhead sprinkler watering late in the day."
    },
    "Tomato___Bacterial_spot": {
        "crop": "Tomato",
        "condition": "Bacterial Spot",
        "severity": "High",
        "recommendation": "Apply copper bactericides with mancozeb. Avoid working among wet plants and avoid overhead irrigation."
    },
    "Tomato___Early_blight": {
        "crop": "Tomato",
        "condition": "Early Blight",
        "severity": "Moderate",
        "recommendation": "Mulch around base to prevent soil splash. Prune bottom leaves and apply organic copper soap spray."
    },
    "Tomato___Late_blight": {
        "crop": "Tomato",
        "condition": "Late Blight",
        "severity": "Critical",
        "recommendation": "Aggressive pathogen: immediately apply copper or chlorothalonil fungicides. Remove and discard heavily diseased tissue."
    },
    "Tomato___Leaf_Mold": {
        "crop": "Tomato",
        "condition": "Leaf Mold",
        "severity": "Moderate",
        "recommendation": "Improve greenhouse/field ventilation to reduce relative humidity below 85%. Apply biofungicide if necessary."
    },
    "Tomato___Septoria_leaf_spot": {
        "crop": "Tomato",
        "condition": "Septoria Leaf Spot",
        "severity": "Moderate to High",
        "recommendation": "Remove infected lower leaves promptly. Water at root base and spray copper fungicide."
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "crop": "Tomato",
        "condition": "Spider Mites",
        "severity": "Moderate",
        "recommendation": "Spray insecticidal soap or neem oil thoroughly under leaves. Encourage predatory mites."
    },
    "Tomato___Target_Spot": {
        "crop": "Tomato",
        "condition": "Target Spot",
        "severity": "Moderate",
        "recommendation": "Improve air circulation. Apply protective fungicides and remove infected leaves."
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "crop": "Tomato",
        "condition": "Yellow Leaf Curl Virus",
        "severity": "High",
        "recommendation": "Transmitted by whiteflies. Control whitefly populations using yellow sticky traps and horticultural oils."
    },
    "Tomato___Tomato_mosaic_virus": {
        "crop": "Tomato",
        "condition": "Mosaic Virus",
        "severity": "High",
        "recommendation": "No cure once infected: remove and destroy infected plants immediately. Disinfect gardening tools with 10% bleach."
    },
    "Tomato___healthy": {
        "crop": "Tomato",
        "condition": "Healthy",
        "severity": "None",
        "recommendation": "Tomato plant is healthy and thriving. Keep soil consistently moist and monitor for early pests."
    }
}
