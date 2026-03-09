"""
JournalFit AI — Curated Journal Knowledge Base
~65 journals across major research domains
"""

JOURNAL_DB = [
    # ─── Biomedical Optics / Medical Imaging ───
    {
        "name": "Biomedical Optics Express",
        "publisher": "Optica Publishing Group",
        "impact_factor": 3.8,
        "quartile": "Q1",
        "avg_review_days": 28,
        "frequency": "Monthly",
        "scope_keywords": [
            "optical coherence tomography", "OCT", "retinal imaging", "ophthalmology",
            "biomedical optics", "photoacoustics", "fluorescence imaging", "tissue optics",
            "light scattering", "optical biopsy", "laser imaging", "microscopy",
            "spectroscopy", "diffuse optical tomography", "optical microscopy",
            "texture analysis", "image segmentation", "retinal layer", "fundus imaging",
            "endoscopy", "in vivo imaging"
        ],
        "aims": "Biomedical Optics Express is a principal outlet for serving the biomedical optics community with rapid review and publication. The journal's scope encompasses fundamental research, technology development, and biomedical studies in all aspects of optics and photonics in the biological and medical sciences.",
        "url": "https://opg.optica.org/boe/home.cfm",
        "supported_types": ["Scientific", "Experimental", "Computational"],
        "sample_paper": "Non-invasive retinal imaging using full-field optical coherence tomography"
    },
    {
        "name": "Optics Express",
        "publisher": "Optica Publishing Group",
        "impact_factor": 3.7,
        "quartile": "Q1",
        "avg_review_days": 35,
        "frequency": "Biweekly",
        "scope_keywords": [
            "optics", "photonics", "lasers", "OCT", "optical coherence", "waveguides",
            "interferometry", "holography", "fiber optics", "imaging systems",
            "nanophotonics", "spectroscopy", "optical sensors", "beam optics",
            "microscopy", "optical microscopy", "retinal", "biomedical"
        ],
        "aims": "Covers all areas of optics and photonics including theory and experiment.",
        "sample_paper": "Advancements in fiber optic sensing for industrial applications"
    },
    {
        "name": "Journal of Biomedical Optics",
        "publisher": "SPIE",
        "impact_factor": 3.0,
        "quartile": "Q2",
        "avg_review_days": 42,
        "frequency": "Monthly",
        "scope_keywords": [
            "biomedical optics", "optical coherence tomography", "OCT", "retinal imaging",
            "tissue spectroscopy", "fluorescence", "laser therapy", "photodynamic therapy",
            "photoacoustic imaging", "diffuse optics", "optical biopsy",
            "retinal layer", "texture analysis", "image analysis"
        ],
        "aims": "Covers optical methods in biomedicine, diagnostics, and therapy."
    },
    {
        "name": "Translational Vision Science & Technology",
        "publisher": "ARVO",
        "impact_factor": 2.9,
        "quartile": "Q2",
        "avg_review_days": 60,
        "frequency": "Monthly",
        "scope_keywords": [
            "retinal imaging", "ophthalmology", "vision science", "OCT", "fundus photography",
            "macular degeneration", "glaucoma", "optic nerve", "retinal layer segmentation",
            "image analysis", "retinal thickness"
        ],
        "aims": "Focuses on visions science and translational research from bench to clinical applications."
    },
    {
        "name": "Investigative Ophthalmology & Visual Science",
        "publisher": "ARVO",
        "impact_factor": 4.2,
        "quartile": "Q1",
        "avg_review_days": 55,
        "frequency": "Monthly",
        "scope_keywords": [
            "ophthalmology", "retina", "retinal imaging", "OCT", "glaucoma",
            "macular degeneration", "vision", "optic nerve", "corneal imaging",
            "retinal layer", "photoreceptors", "retinal thickness map"
        ],
        "aims": "Publishes research in ophthalmology, visual science, and visual system disorders."
    },
    {
        "name": "Optics Letters",
        "publisher": "Optica Publishing Group",
        "impact_factor": 3.6,
        "quartile": "Q1",
        "avg_review_days": 22,
        "frequency": "Biweekly",
        "scope_keywords": [
            "optics", "photonics", "lasers", "interferometry", "OCT", "fiber optics",
            "nonlinear optics", "optical sensors", "imaging", "spectroscopy"
        ],
        "aims": "Short rapid communications covering all areas of optics and photonics."
    },
    {
        "name": "IEEE Transactions on Medical Imaging",
        "publisher": "IEEE",
        "impact_factor": 10.6,
        "quartile": "Q1",
        "avg_review_days": 90,
        "frequency": "Monthly",
        "scope_keywords": [
            "medical imaging", "image analysis", "retinal imaging", "deep learning",
            "CT", "MRI", "OCT", "image segmentation", "texture analysis",
            "convolutional neural network", "biomedical imaging", "layer segmentation",
            "optical coherence tomography"
        ],
        "aims": "Covers the theory, design, and application of medical imaging systems and analysis."
    },
    {
        "name": "Medical Image Analysis",
        "publisher": "Elsevier",
        "impact_factor": 10.9,
        "quartile": "Q1",
        "avg_review_days": 95,
        "frequency": "Monthly",
        "scope_keywords": [
            "medical imaging", "image analysis", "machine learning", "deep learning",
            "segmentation", "texture analysis", "retinal imaging", "OCT",
            "feature extraction", "convolutional neural networks", "biomedical imaging"
        ],
        "aims": "Publishes research on algorithms, methodology and applications of medical image analysis."
    },
    {
        "name": "Computers in Biology and Medicine",
        "publisher": "Elsevier",
        "impact_factor": 7.0,
        "quartile": "Q1",
        "avg_review_days": 50,
        "frequency": "Monthly",
        "scope_keywords": [
            "biomedical", "image analysis", "machine learning", "texture analysis",
            "retinal analysis", "OCT", "deep learning", "classification",
            "signal processing", "disease detection"
        ],
        "aims": "Covers computational methods applied to biology and medicine."
    },
    {
        "name": "Scientific Reports",
        "publisher": "Nature Publishing Group",
        "impact_factor": 3.8,
        "quartile": "Q1",
        "avg_review_days": 90,
        "frequency": "Weekly",
        "scope_keywords": [
            "multidisciplinary", "biomedical", "optics", "retinal", "imaging",
            "machine learning", "texture analysis", "OCT", "physics", "biology",
            "computational methods", "image processing"
        ],
        "aims": "Open access journal covering all areas of natural sciences."
    },
    {
        "name": "PLOS ONE",
        "publisher": "PLOS",
        "impact_factor": 3.7,
        "quartile": "Q1",
        "avg_review_days": 120,
        "frequency": "Weekly",
        "scope_keywords": [
            "multidisciplinary", "biomedical", "optics", "imaging", "clinical",
            "computational", "texture analysis", "machine learning", "biology"
        ],
        "aims": "Open access multidisciplinary journal publishing peer-reviewed research."
    },

    # ─── Machine Learning / AI ───
    {
        "name": "Nature Machine Intelligence",
        "publisher": "Nature Publishing Group",
        "impact_factor": 23.8,
        "quartile": "Q1",
        "avg_review_days": 120,
        "frequency": "Monthly",
        "scope_keywords": [
            "machine learning", "deep learning", "artificial intelligence", "neural networks",
            "reinforcement learning", "natural language processing", "computer vision",
            "generative models", "transfer learning", "large language models"
        ],
        "aims": "Publishes research on artificial intelligence and machine learning with broad impact."
    },
    {
        "name": "IEEE Transactions on Neural Networks and Learning Systems",
        "publisher": "IEEE",
        "impact_factor": 10.4,
        "quartile": "Q1",
        "avg_review_days": 80,
        "frequency": "Monthly",
        "scope_keywords": [
            "neural networks", "deep learning", "machine learning", "learning systems",
            "classification", "regression", "convolutional neural networks", "RNN",
            "transfer learning", "optimization", "supervised learning"
        ],
        "aims": "Covers theory, design, and applications of neural networks and learning systems."
    },
    {
        "name": "Pattern Recognition",
        "publisher": "Elsevier",
        "impact_factor": 7.5,
        "quartile": "Q1",
        "avg_review_days": 70,
        "frequency": "Monthly",
        "scope_keywords": [
            "pattern recognition", "machine learning", "image classification",
            "feature extraction", "texture analysis", "deep learning", "convolutional networks",
            "object detection", "image segmentation", "computer vision"
        ],
        "aims": "Covers pattern recognition including statistical, syntactic, and neural approaches."
    },
    {
        "name": "Expert Systems with Applications",
        "publisher": "Elsevier",
        "impact_factor": 7.5,
        "quartile": "Q1",
        "avg_review_days": 55,
        "frequency": "Biweekly",
        "scope_keywords": [
            "AI", "machine learning", "expert systems", "deep learning", "classification",
            "data mining", "natural language processing", "prediction", "optimization"
        ],
        "aims": "Focuses on artificial intelligence and machine learning applications."
    },
    {
        "name": "Knowledge-Based Systems",
        "publisher": "Elsevier",
        "impact_factor": 7.2,
        "quartile": "Q1",
        "avg_review_days": 60,
        "frequency": "Biweekly",
        "scope_keywords": [
            "knowledge-based systems", "machine learning", "AI", "classification",
            "neural networks", "fuzzy logic", "data mining", "recommender systems"
        ],
        "aims": "Covers knowledge-based systems, machine learning, and intelligent systems."
    },
    {
        "name": "Neurocomputing",
        "publisher": "Elsevier",
        "impact_factor": 5.5,
        "quartile": "Q1",
        "avg_review_days": 55,
        "frequency": "Biweekly",
        "scope_keywords": [
            "neural networks", "deep learning", "machine learning", "classification",
            "image recognition", "convolutional networks", "pattern recognition",
            "feature learning", "reinforcement learning"
        ],
        "aims": "Covers neural computation and machine learning research."
    },
    {
        "name": "Artificial Intelligence in Medicine",
        "publisher": "Elsevier",
        "impact_factor": 6.1,
        "quartile": "Q1",
        "avg_review_days": 65,
        "frequency": "Monthly",
        "scope_keywords": [
            "AI in medicine", "machine learning", "clinical decision support",
            "medical imaging AI", "deep learning", "biomedical data",
            "computer-aided diagnosis", "image classification"
        ],
        "aims": "Covers AI methods applied to medical diagnosis, therapy, and monitoring."
    },
    {
        "name": "Applied Soft Computing",
        "publisher": "Elsevier",
        "impact_factor": 7.2,
        "quartile": "Q1",
        "avg_review_days": 55,
        "frequency": "Monthly",
        "scope_keywords": [
            "soft computing", "fuzzy logic", "neural networks", "machine learning",
            "evolutionary computation", "optimization", "classification", "clustering"
        ],
        "aims": "Covers fuzzy, neural, evolutionary and probabilistic computing methods."
    },

    # ─── Computer Science / Engineering ───
    {
        "name": "IEEE Transactions on Image Processing",
        "publisher": "IEEE",
        "impact_factor": 10.8,
        "quartile": "Q1",
        "avg_review_days": 85,
        "frequency": "Monthly",
        "scope_keywords": [
            "image processing", "image analysis", "computer vision", "segmentation",
            "texture analysis", "feature extraction", "deep learning", "restoration",
            "compression", "super resolution", "object detection"
        ],
        "aims": "Covers theory and applications of image and video processing."
    },
    {
        "name": "Computer Vision and Image Understanding",
        "publisher": "Elsevier",
        "impact_factor": 4.3,
        "quartile": "Q1",
        "avg_review_days": 70,
        "frequency": "Monthly",
        "scope_keywords": [
            "computer vision", "image understanding", "scene recognition", "segmentation",
            "object detection", "deep learning", "texture analysis", "3D reconstruction"
        ],
        "aims": "Covers methods for interpreting and understanding digital imagery."
    },
    {
        "name": "Signal Processing",
        "publisher": "Elsevier",
        "impact_factor": 4.4,
        "quartile": "Q1",
        "avg_review_days": 60,
        "frequency": "Monthly",
        "scope_keywords": [
            "signal processing", "image processing", "filtering", "spectral analysis",
            "texture analysis", "feature extraction", "wavelet", "Fourier"
        ],
        "aims": "Covers all aspects of theory and practice in signal processing."
    },
    {
        "name": "IEEE Access",
        "publisher": "IEEE",
        "impact_factor": 3.9,
        "quartile": "Q2",
        "avg_review_days": 30,
        "frequency": "Weekly",
        "scope_keywords": [
            "engineering", "computer science", "machine learning", "imaging",
            "signal processing", "biomedical engineering", "electronics",
            "systems", "applications"
        ],
        "aims": "Multidisciplinary open access journal covering all IEEE fields of interest."
    },

    # ─── Physics ───
    {
        "name": "Physical Review Applied",
        "publisher": "APS",
        "impact_factor": 4.0,
        "quartile": "Q1",
        "avg_review_days": 60,
        "frequency": "Monthly",
        "scope_keywords": [
            "applied physics", "photonics", "optics", "condensed matter",
            "materials", "semiconductor", "nano", "sensors", "imaging systems"
        ],
        "aims": "Covers application-oriented physics bridging fundamental physics and applied areas."
    },
    {
        "name": "Optica",
        "publisher": "Optica Publishing Group",
        "impact_factor": 10.4,
        "quartile": "Q1",
        "avg_review_days": 40,
        "frequency": "Monthly",
        "scope_keywords": [
            "optics", "photonics", "lasers", "nonlinear optics", "quantum optics",
            "optical microscopy", "imaging", "spectroscopy", "fiber optics"
        ],
        "aims": "High-impact journal publishing significant advances in optics and photonics."
    },
    {
        "name": "Light: Science & Applications",
        "publisher": "Nature Publishing Group",
        "impact_factor": 19.4,
        "quartile": "Q1",
        "avg_review_days": 70,
        "frequency": "Monthly",
        "scope_keywords": [
            "light", "photonics", "optics", "lasers", "optical imaging",
            "nanophotonics", "optical systems", "biophotonics"
        ],
        "aims": "High-impact open access journal covering all aspects of photonics and optics."
    },
    {
        "name": "Applied Physics Letters",
        "publisher": "AIP Publishing",
        "impact_factor": 4.0,
        "quartile": "Q1",
        "avg_review_days": 25,
        "frequency": "Weekly",
        "scope_keywords": [
            "applied physics", "photonics", "semiconductor", "nano", "optics",
            "materials", "sensors", "lasers", "quantum"
        ],
        "aims": "Short rapid communications in applied physics and photonics."
    },

    # ─── Environmental / Earth Sciences ───
    {
        "name": "Remote Sensing of Environment",
        "publisher": "Elsevier",
        "impact_factor": 11.1,
        "quartile": "Q1",
        "avg_review_days": 80,
        "frequency": "Biweekly",
        "scope_keywords": [
            "remote sensing", "satellite imagery", "land cover", "vegetation",
            "climate", "earth observation", "spectral analysis", "image classification",
            "texture analysis", "geospatial"
        ],
        "aims": "Covers remote sensing methods and applications for earth observation."
    },
    {
        "name": "ISPRS Journal of Photogrammetry and Remote Sensing",
        "publisher": "Elsevier",
        "impact_factor": 10.6,
        "quartile": "Q1",
        "avg_review_days": 85,
        "frequency": "Biweekly",
        "scope_keywords": [
            "remote sensing", "photogrammetry", "LiDAR", "satellite", "3D",
            "image analysis", "geospatial", "land use", "urban mapping"
        ],
        "aims": "Official journal of ISPRS covering photogrammetry and remote sensing."
    },
    {
        "name": "Environmental Science & Technology",
        "publisher": "ACS",
        "impact_factor": 10.8,
        "quartile": "Q1",
        "avg_review_days": 50,
        "frequency": "Biweekly",
        "scope_keywords": [
            "environmental chemistry", "pollution", "water treatment", "air quality",
            "toxicology", "sustainability", "climate change", "environmental monitoring"
        ],
        "aims": "Covers environmental science and engineering across all environmental media."
    },

    # ─── Biology / Life Sciences ───
    {
        "name": "Nature Biomedical Engineering",
        "publisher": "Nature Publishing Group",
        "impact_factor": 25.0,
        "quartile": "Q1",
        "avg_review_days": 130,
        "frequency": "Monthly",
        "scope_keywords": [
            "biomedical engineering", "tissue engineering", "imaging", "diagnostics",
            "therapuetics", "biosensors", "nanotechnology", "biomaterials"
        ],
        "aims": "High-impact journal covering research at the intersection of engineering and biology."
    },
    {
        "name": "Cells",
        "publisher": "MDPI",
        "impact_factor": 5.1,
        "quartile": "Q2",
        "avg_review_days": 35,
        "frequency": "Monthly",
        "scope_keywords": [
            "cell biology", "molecular biology", "genetics", "biochemistry",
            "cell signaling", "cell imaging", "genomics", "proteomics"
        ],
        "aims": "Open access journal covering all aspects of cell biology."
    },

    # ─── Electronics / Engineering ───
    {
        "name": "Sensors",
        "publisher": "MDPI",
        "impact_factor": 3.9,
        "quartile": "Q2",
        "avg_review_days": 28,
        "frequency": "Biweekly",
        "scope_keywords": [
            "sensors", "sensing", "IoT", "optical sensor", "image sensor",
            "biological sensors", "chemical sensors", "signal processing",
            "wearable", "MEMS"
        ],
        "aims": "Open access journal covering all aspects of sensor science and technology."
    },
    {
        "name": "Electronics",
        "publisher": "MDPI",
        "impact_factor": 2.9,
        "quartile": "Q2",
        "avg_review_days": 20,
        "frequency": "Biweekly",
        "scope_keywords": [
            "electronics", "circuits", "signal processing", "embedded systems",
            "FPGA", "communication", "control systems", "IoT"
        ],
        "aims": "Open access journal covering electronics research and applications."
    },
    {
        "name": "IEEE Transactions on Biomedical Engineering",
        "publisher": "IEEE",
        "impact_factor": 4.8,
        "quartile": "Q1",
        "avg_review_days": 75,
        "frequency": "Monthly",
        "scope_keywords": [
            "biomedical engineering", "biosignal processing", "medical imaging",
            "wearable sensors", "neural engineering", "biosensors",
            "physiological monitoring", "tissue engineering"
        ],
        "aims": "Covers the intersection of engineering principles and biological systems."
    },
    {
        "name": "Biomedical Signal Processing and Control",
        "publisher": "Elsevier",
        "impact_factor": 4.9,
        "quartile": "Q1",
        "avg_review_days": 55,
        "frequency": "Monthly",
        "scope_keywords": [
            "biomedical signal processing", "ECG", "EEG", "medical imaging",
            "image analysis", "feature extraction", "classification", "retinal"
        ],
        "aims": "Covers signal and image processing applied to biomedical data."
    },

    # ─── Chemistry ───
    {
        "name": "Analytical Chemistry",
        "publisher": "ACS",
        "impact_factor": 6.7,
        "quartile": "Q1",
        "avg_review_days": 50,
        "frequency": "Biweekly",
        "scope_keywords": [
            "analytical chemistry", "spectroscopy", "chromatography", "sensors",
            "mass spectrometry", "electrochemistry", "detection", "biosensors"
        ],
        "aims": "Covers fundamental and applied aspects of analytical chemistry."
    },
    {
        "name": "Journal of Physical Chemistry B",
        "publisher": "ACS",
        "impact_factor": 3.4,
        "quartile": "Q2",
        "avg_review_days": 40,
        "frequency": "Weekly",
        "scope_keywords": [
            "physical chemistry", "biophysics", "soft matter", "spectroscopy",
            "membranes", "colloids", "proteins", "molecular dynamics"
        ],
        "aims": "Covers physical chemistry of soft matter, biophysics, and complex materials."
    },

    # ─── Materials Science ───
    {
        "name": "Advanced Materials",
        "publisher": "Wiley",
        "impact_factor": 27.4,
        "quartile": "Q1",
        "avg_review_days": 90,
        "frequency": "Weekly",
        "scope_keywords": [
            "materials science", "nanomaterials", "photonics", "biomaterials",
            "polymers", "semiconductors", "thin films", "nanostructures"
        ],
        "aims": "High-impact journal covering all aspects of materials science and engineering."
    },
    {
        "name": "ACS Nano",
        "publisher": "ACS",
        "impact_factor": 15.8,
        "quartile": "Q1",
        "avg_review_days": 60,
        "frequency": "Monthly",
        "scope_keywords": [
            "nanotechnology", "nanomaterials", "nanoparticles", "biosensors",
            "quantum dots", "graphene", "carbon nanotubes", "nanophotonics"
        ],
        "aims": "Covers fundamental and applied aspects of nanoscale science and technology."
    },

    # ─── Clinical / Medical ───
    {
        "name": "British Journal of Ophthalmology",
        "publisher": "BMJ",
        "impact_factor": 4.1,
        "quartile": "Q1",
        "avg_review_days": 80,
        "frequency": "Monthly",
        "scope_keywords": [
            "ophthalmology", "retina", "glaucoma", "macular degeneration",
            "OCT", "retinal imaging", "cornea", "optic nerve", "visual acuity"
        ],
        "aims": "Covers clinical and experimental ophthalmology and visual sciences."
    },
    {
        "name": "Graefe's Archive for Clinical and Experimental Ophthalmology",
        "publisher": "Springer",
        "impact_factor": 2.8,
        "quartile": "Q2",
        "avg_review_days": 70,
        "frequency": "Monthly",
        "scope_keywords": [
            "ophthalmology", "retinal disease", "OCT imaging", "retinal layers",
            "vitreoretinal", "glaucoma", "diabetic retinopathy", "macular"
        ],
        "aims": "Covers clinical and experimental research in ophthalmology."
    },
    {
        "name": "Retina",
        "publisher": "Lippincott Williams & Wilkins",
        "impact_factor": 4.0,
        "quartile": "Q1",
        "avg_review_days": 75,
        "frequency": "Monthly",
        "scope_keywords": [
            "retina", "retinal diseases", "vitreoretinal surgery", "OCT",
            "retinal imaging", "macular degeneration", "diabetic retinopathy",
            "retinal thickness", "retinal layer"
        ],
        "aims": "Covers clinical and basic research in diseases of the retina and vitreous."
    },
    {
        "name": "Ophthalmology",
        "publisher": "Elsevier",
        "impact_factor": 13.7,
        "quartile": "Q1",
        "avg_review_days": 90,
        "frequency": "Monthly",
        "scope_keywords": [
            "ophthalmology", "clinical trials", "retinal disease", "glaucoma",
            "cataract", "cornea", "OCT", "retinal imaging", "visual outcomes"
        ],
        "aims": "Official journal of the American Academy of Ophthalmology."
    },

    # ─── Data Science / Statistics ───
    {
        "name": "Information Fusion",
        "publisher": "Elsevier",
        "impact_factor": 14.7,
        "quartile": "Q1",
        "avg_review_days": 75,
        "frequency": "Monthly",
        "scope_keywords": [
            "data fusion", "machine learning", "deep learning", "multimodal",
            "sensor fusion", "image fusion", "classification", "ensemble methods"
        ],
        "aims": "Covers architectures, algorithms and applications of information fusion."
    },
    {
        "name": "IEEE Transactions on Fuzzy Systems",
        "publisher": "IEEE",
        "impact_factor": 11.9,
        "quartile": "Q1",
        "avg_review_days": 65,
        "frequency": "Monthly",
        "scope_keywords": [
            "fuzzy systems", "fuzzy logic", "soft computing", "classification",
            "control", "decision making", "uncertainty"
        ],
        "aims": "Covers fuzzy set theory and its applications in engineering and computer science."
    },

    # ─── Multidisciplinary ───
    {
        "name": "Nature",
        "publisher": "Nature Publishing Group",
        "impact_factor": 64.8,
        "quartile": "Q1",
        "avg_review_days": 150,
        "frequency": "Weekly",
        "scope_keywords": [
            "science", "multidisciplinary", "biology", "physics", "chemistry",
            "medicine", "breakthrough", "discovery"
        ],
        "aims": "One of the world's most prestigious scientific journals, covering all fields."
    },
    {
        "name": "Science",
        "publisher": "AAAS",
        "impact_factor": 56.9,
        "quartile": "Q1",
        "avg_review_days": 150,
        "frequency": "Weekly",
        "scope_keywords": [
            "science", "multidisciplinary", "breakthrough discovery",
            "physics", "biology", "chemistry", "medicine", "technology"
        ],
        "aims": "Publishes outstanding research with broad scientific significance."
    },
    {
        "name": "Frontiers in Physics",
        "publisher": "Frontiers",
        "impact_factor": 2.7,
        "quartile": "Q2",
        "avg_review_days": 45,
        "frequency": "Monthly",
        "scope_keywords": [
            "physics", "optics", "photonics", "applied physics",
            "condensed matter", "astrophysics", "biophysics"
        ],
        "aims": "Open access journal covering all areas of physics."
    },
    {
        "name": "Heliyon",
        "publisher": "Elsevier",
        "impact_factor": 4.0,
        "quartile": "Q2",
        "avg_review_days": 40,
        "frequency": "Monthly",
        "scope_keywords": [
            "multidisciplinary", "science", "engineering", "medicine",
            "biomedical", "image analysis", "optics"
        ],
        "aims": "Open access multidisciplinary journal publishing research across all disciplines."
    },
    {
        "name": "MDPI Applied Sciences",
        "publisher": "MDPI",
        "impact_factor": 2.7,
        "quartile": "Q3",
        "avg_review_days": 20,
        "frequency": "Biweekly",
        "scope_keywords": [
            "applied sciences", "engineering", "biomedical", "optics",
            "image processing", "machine learning", "sensors", "materials"
        ],
        "aims": "Open access journal covering applied science and engineering."
    },
    {
        "name": "Journal of Imaging",
        "publisher": "MDPI",
        "impact_factor": 2.9,
        "quartile": "Q3",
        "avg_review_days": 25,
        "frequency": "Monthly",
        "scope_keywords": [
            "imaging", "image processing", "medical imaging", "texture analysis",
            "segmentation", "image classification", "feature extraction"
        ],
        "aims": "Open access journal covering all aspects of imaging science and technology."
    },
    # ─── Photonics ───
    {
        "name": "Photonics",
        "publisher": "MDPI",
        "impact_factor": 2.1,
        "quartile": "Q3",
        "avg_review_days": 22,
        "frequency": "Monthly",
        "scope_keywords": [
            "photonics", "optics", "laser", "optical fiber", "integrated photonics",
            "optical coherence", "OCT", "optical microscopy", "photonic devices"
        ],
        "aims": "Open access journal covering photonics research and applications."
    },
]
