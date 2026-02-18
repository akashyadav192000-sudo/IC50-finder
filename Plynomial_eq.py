import numpy as np
import streamlit as st

st.header("Find your IC50 (Ms. Simran Nain)")

# Use st.text_input instead of input()
# input() stops the server console; st.text_input creates a box in the browser.
coe = st.text_input("Enter the coefficient values (separated by commas)")

# Check if data is entered before running the math
if coe:
    try:
        coefficients = [float(x.strip()) for x in coe.split(",") if x.strip() != ""]
        
        # Define the target Y value
        y = 50

        # Create a copy to avoid modifying the original display if needed later
        calc_coeffs = coefficients.copy()
        
        calc_coeffs[-1] -= y

        # Calculate roots
        root_val = np.roots(calc_coeffs)

        # 4. Display results using Streamlit widgets
        st.success(f"The calculated X values (IC50) are:")
        st.write(root_val)
        
        # Optional: Filter for real, positive roots (common for concentration)
        real_roots = [r.real for r in root_val if np.isreal(r) and r.real > 0]
        if real_roots:
            st.info(f"Most likely concentration (positive real root): {real_roots[0]:.4f}")

    except ValueError:
        st.error("Please ensure you entered only numbers separated by commas.")
    except Exception as e:
        st.error(f"An error occurred: {e}")