import math

import torch
import torch.nn as nn

__all__ = ['model']


class model(nn.Module):
    def __init__(self, in_channels=10, num_labels=4):
        super(model, self).__init__()

        self.conv_1 = nn.Sequential(
            nn.Conv2d(in_channels=in_channels, out_channels=16,
                      kernel_size=1, stride=1, padding=0),
            nn.ReLU(inplace=True),
            nn.Conv2d(in_channels=16, out_channels=16,
                      kernel_size=3, stride=1, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(in_channels=16, out_channels=32,
                      kernel_size=3, stride=2, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(in_channels=32, out_channels=16,
                      kernel_size=3, stride=1, padding=1)
        )

        self._init_weight()
        self.dump_patches = True

    # initialize weights
    def _init_weight(self):
        for layer in self.modules():
            if isinstance(layer, nn.Conv2d):
                n = layer.kernel_size[0] * \
                    layer.kernel_size[1] * layer.out_channels
                layer.weight.data.normal_(0, math.sqrt(2. / n))
                if layer.bias is not None:
                    layer.bias.data.fill_(0)

    # forward propagation
    def forward(self, x):
        shallow_feature_1 = self.conv_1(x)

        return output_feature

