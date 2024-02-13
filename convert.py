from PIL import Image
import numpy as np

def resize_image(png_path, scale_factor):
    try:
        # Open the PNG image
        png_image = Image.open(png_path)

        # Calculate new width and height
        width, height = png_image.size
        new_width = int(width * scale_factor)
        new_height = int(height * scale_factor)

        # Resize the image
        resized_image = png_image.resize((new_width, new_height))

        return resized_image

    except Exception as e:
        print(f"An error occurred while resizing the image: {e}")
        return None

def png_to_svg(png_path, svg_path):
    try:
        # Resize the input image to 75% of its original size
        resized_image = resize_image(png_path, 0.25)

        if resized_image:
            # Convert the resized image to RGBA mode to handle transparency
            resized_image = resized_image.convert("RGBA")

            # Get image data as numpy array
            img_array = np.array(resized_image)

            # Extract dimensions
            width, height = resized_image.size

            # Create SVG content
            svg_content = f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">\n'

            for y in range(height):
                for x in range(width):
                    # Get RGBA values
                    r, g, b, a = img_array[y][x]

                    # Convert to hex format
                    color_hex = f'#{r:02x}{g:02x}{b:02x}'

                    # Only add rectangle if pixel is not fully transparent
                    if a > 0:
                        svg_content += f'<rect x="{x}" y="{y}" width="1" height="1" fill="{color_hex}" opacity="{a/255:.2f}"/>\n'

            # Close SVG content
            svg_content += '</svg>'

            # Write SVG content to file
            with open(svg_path, 'w') as svg_file:
                svg_file.write(svg_content)

            print(f"SVG file saved to {svg_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace "input.png" and "output.svg" with your input PNG file and desired output SVG file name
    input_path = "input.png"
    output_path = "output.svg"
    png_to_svg(input_path, output_path)
