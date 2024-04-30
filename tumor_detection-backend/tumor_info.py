# tumor_info.py

precautions_dict = {
    'glioma': 'Regular check-ups with neurologist/oncologist • Adherence to prescribed medication regimen (chemotherapy, targeted therapy, etc.) • Lifestyle modifications (healthy diet, regular exercise, stress reduction) • Awareness of worsening symptoms (seizures, changes in personality, cognitive decline) • Prompt medical attention for any concerning symptoms (increased headache severity, new neurological deficits, nausea/vomiting)',
    'meningioma': 'Regular check-ups with neurologist/neurosurgeon • Adherence to prescribed medication regimen (steroids, anti-seizure medications, etc.) • Lifestyle modifications (maintaining a healthy weight, regular exercise, stress management) • Awareness of worsening symptoms (headaches, changes in vision, weakness or numbness) • Prompt medical attention for any concerning symptoms (rapidly worsening headaches, seizures, loss of consciousness)',
    'no tumor': 'No specific precautions needed.',
    'pituitary': 'Regular check-ups with endocrinologist/neurologist • Adherence to prescribed medication regimen • Lifestyle modifications (healthy diet, stress management, adequate sleep) • Awareness of worsening symptoms (sudden vision changes, severe headaches, neurological deficits) • Prompt medical attention for any concerning symptoms'
}

symptoms_dict = {
    'glioma': 'Headaches (often severe and persistent) • Seizures • Cognitive changes (memory loss, confusion) • Weakness or numbness in limbs • Changes in personality or mood • Nausea and vomiting',
    'meningioma': 'Headaches (usually dull and persistent) • Changes in vision (blurred vision, loss of peripheral vision) • Weakness or numbness in limbs • Seizures • Changes in personality or behavior • Cognitive changes (memory problems, difficulty concentrating)',
    'no tumor': 'No specific symptoms detected.',
    'pituitary': 'Headaches • Vision problems (blurry or double vision) • Hormonal imbalances (irregular menstruation, changes in libido) • Unexplained weight gain or loss • Fatigue, nausea, weakness • Neurological symptoms (seizures, cognitive changes)'
}

tumor_urls = {
    'glioma': {
        'precautions_url': 'https://www.mayoclinic.org/diseases-conditions/glioma/diagnosis-treatment/drc-20350255',
        'symptoms_url': 'https://www.mayoclinic.org/diseases-conditions/glioma/symptoms-causes/syc-20350251'
    },
    'meningioma': {
        'precautions_url': 'https://my.clevelandclinic.org/health/diseases/17858-meningioma',
        'symptoms_url': 'https://www.pennmedicine.org/for-patients-and-visitors/patient-information/conditions-treated-a-to-z/meningioma'
    },
    'pituitary': {
        'precautions_url': 'https://www.mdanderson.org/cancerwise/foods-to-avoid-with-pituitary-tumors.h00-159618645.html',
        'symptoms_url': 'https://www.cancer.net/cancer-types/pituitary-gland-tumor/symptoms-and-signs'
    },
    # Add URLs for other tumor types as needed
}