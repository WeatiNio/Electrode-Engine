def draw_text(screen, font, text, position, colour):
    text_surface = font.render(text, True, colour)
    text_rect = text_surface.get_rect(center=position)

    screen.blit(text_surface, text_rect)